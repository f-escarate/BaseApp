import datetime
from fastapi import Form, UploadFile
from pydantic import BaseModel


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

# ================ Users schemas ================ #
@form_body
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    password2: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
@form_body
class ChangePassword(BaseModel):
    old_pass: str
    new_pass: str


# ================ Item schemas ================ #
    
@form_body
class Item(BaseModel):
    title: str
    description: str
    continuousVar: float
    discreteVar: int
    date: datetime.date
    image: UploadFile
