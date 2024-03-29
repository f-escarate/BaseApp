from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from schemas import ChangePassword, Item, UserRegister
from authentication import authenticate_user, create_access_token, get_password_hash, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, get_user_by_name, unauthorized_exception, verify_password
from utils import save_image, create_item, read_image, img_validation
from database import get_db, Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8000",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/post_item/")
async def post_item(token: Annotated[str, Depends(oauth2_scheme)], item: Item = Depends(Item), db: Session = Depends(get_db)):
    if not token:
        return unauthorized_exception("Invalid token")
    user = get_user_by_name(jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub"), db)
    if user is None:
        return {"status": "error", "msg": "problem with user authentication"}
    file_extension = img_validation(item.image)
    if file_extension is None:
        return {"status": "error", "msg": "invalid image"}
        
    image = item.image
    item.image = file_extension
    created_item = create_item(db=db, item=item, user_id=user.id)
    save_image(image, created_item.id, file_extension)
    return {"status": "success"}

@app.get("/get_items/")
async def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.get("/get_items/own/")
async def get_my_items(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    if not token:
        return unauthorized_exception("Invalid token")
    user = get_user_by_name(jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub"), db)
    if user is None:
        return {"status": "error", "msg": "problem with user authentication"}
    items = db.query(models.Item).filter(models.Item.owner_id == user.id).all()
    return items

@app.get("/get_item/{item_id}/")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

@app.patch("/update_item/{item_id}/")
async def update_item(token: Annotated[str, Depends(oauth2_scheme)], item_id: int, item: Item = Depends(Item), db: Session = Depends(get_db)):
    if not token:
        return unauthorized_exception("Invalid token")
    user = get_user_by_name(jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub"), db)
    if user is None:
        return {"status": "error", "msg": "problem with user authentication"}
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        return {"status": "error", "msg": "item does not exist"}
    if db_item.owner_id != user.id:
        return {"status": "error", "msg": "you are not the owner of this item"}
    file_extension = img_validation(item.image)
    if file_extension is None:
        return {"status": "error", "msg": "invalid image"}
    image = item.image
    item.image = file_extension
    db_item.title = item.title
    db_item.description = item.description
    db_item.continuousVar = item.continuousVar
    db_item.discreteVar = item.discreteVar
    db_item.date = item.date
    db_item.image = file_extension
    db.commit()
    save_image(image, item_id, file_extension)
    return {"status": "success"}

@app.get("/get_image/{item_id}")
async def get_image(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    img = read_image(item_id, item.image)
    return Response(content=img, media_type=f"image/{item.image}")

@app.get("/me/")
async def get_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = unauthorized_exception("Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_name(username, db)
    if user is None:
        raise credentials_exception
    return {
        "status": "success",
        "username": user.username,
        "email": user.email
    }

@app.post("/register/")
async def register(user: UserRegister = Depends(UserRegister), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user is not None:
        return {"status": "error", "msg": "username already exists"}
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user is not None:
        return {"status": "error", "msg": "an account with this email already exists"}
    if user.password != user.password2:
        return {"status": "error", "msg": "passwords do not match"}
    new_user = models.User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success"}

@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise unauthorized_exception("Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "status": "success",
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.patch("/change_password/")
async def change_password(token: Annotated[str, Depends(oauth2_scheme)], change: ChangePassword = Depends(ChangePassword), db: Session = Depends(get_db)):
    if not token:
        return unauthorized_exception("Invalid token")
    user = get_user_by_name(jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub"), db)
    if user is None:
        return {"status": "error", "msg": "Problem with user authentication"}
    if not verify_password(change.old_pass, user.hashed_password):
        return {"status": "error", "msg": "Incorrect old password"}
    user.hashed_password = get_password_hash(change.new_pass)
    db.commit()
    return {"status": "success"}

app.mount("/", StaticFiles(directory="static",html = True), name="static")