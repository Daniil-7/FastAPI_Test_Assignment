import datetime
from pydantic import BaseModel


class BaseProduct(BaseModel):
    name: str
    price: int
    image: str


class Product(BaseProduct):
    id: int
    created: datetime.datetime
    updated: datetime.datetime


class ProductIn(BaseProduct):
    pass