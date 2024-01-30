from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from schemas import Item
from utils import save_image, create_item
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
    print(item)
    file_extension = save_image(item.image, item.title)
    if file_extension is None:
        return {"status": "error"}
    item.image = file_extension
    create_item(db=db, item=item)
    return {"status": "success"}