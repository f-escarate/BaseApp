from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from schemas import Item
from utils import save_image, create_item, read_image, img_validation
from database import get_db, Base, engine

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://localhost:8080",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    items = db.query(Item).all()
    return items

@app.get("/get_image/{item_id}")
async def get_image(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    return read_image(item_id, item.image)