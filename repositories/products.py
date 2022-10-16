from typing import List, Optional
import datetime
from models.products import Product, ProductIn
from db.products import products
from .base import BaseRepository
from db.users import users


class ProductRepository(BaseRepository):
    async def create(self, p: ProductIn) -> Product:
        product = Product(
            id=0,
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            name=p.name,
            image=p.image,
            price=p.price,
            category_id=p.category_id,
        )
        values = {**product.dict()}
        values.pop("id", None)
        query = products.insert().values(**values)
        product.id = await self.database.execute(query=query)
        return product

    async def update(self, id: int, p: ProductIn) -> Product:
        product = Product(
            id=id,
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            name=p.name,
            image=p.image,
            price=p.price,
            category_id=p.category_id,
        )
        values = {**product.dict()}
        values.pop("id", None)
        values.pop("created", None)
        query = products.update().where(products.c.id == id).values(**values)
        await self.database.execute(query=query)
        return product

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Product]:
        query = products.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = products.delete().where(products.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Product]:
        query = products.select().where(products.c.id == id)
        product = await self.database.fetch_one(query=query)
        if product is None:
            return None
        return Product.parse_obj(product)
