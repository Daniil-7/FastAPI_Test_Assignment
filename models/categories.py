import datetime
from pydantic import BaseModel


class BaseCategory(BaseModel):
    name: str
    image: str


class Category(BaseCategory):
    id: int
    created: datetime.datetime
    updated: datetime.datetime


class CategoryIn(BaseCategory):
    pass
