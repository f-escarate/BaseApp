from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from schemas import Item, UserRegister
from authentication import authenticate_user, create_access_token, get_password_hash, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, get_user_by_name, unauthorized_exception
from utils import save_image, create_item, read_image, img_validation
from database import get_db, Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/post_item/")
async def post_item(item: Item = Depends(Item), db: Session = Depends(get_db)):
    file_extension = img_validation(item.image)
    if file_extension is None:
        return {"status": "error", "msg": "invalid image"}
        
    image = item.image
    item.image = file_extension
    created_item = create_item(db=db, item=item)
    save_image(image, created_item.id, file_extension)
    return {"status": "success"}

@app.get("/get_items/")
async def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

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