import datetime
import inspect
from typing import Optional, Type
from fastapi import File, Form, UploadFile
from pydantic import BaseModel


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


@form_body
class Item(BaseModel):
    title: str
    description: str
    continuousVar: float
    discreteVar: int
    date: datetime.date
    image: UploadFile
