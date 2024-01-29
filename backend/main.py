from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_models import Item
from utils import save_image

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
async def post_item(item: Item = Depends(Item)):
    print(item)
    save_image(item.image, item.title)
    return "ret"