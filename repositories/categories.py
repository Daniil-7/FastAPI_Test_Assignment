from typing import List, Optional
import datetime
from models.categories import Category, CategoryIn
from db.categories import categories
from .base import BaseRepository
from db.users import users


class CategoryRepository(BaseRepository):
    async def create(self, c: CategoryIn) -> Category:
        category = Category(
            id=0,
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            name=c.name,
            image=c.image,
        )
        values = {**category.dict()}
        values.pop("id", None)
        query = categories.insert().values(**values)
        category.id = await self.database.execute(query=query)
        return category

    async def update(self, id: int, c: CategoryIn) -> Category:
        category = Category(
            id=id,
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            name=c.name,
            image=c.image,
        )
        values = {**category.dict()}
        values.pop("id", None)
        values.pop("created", None)
        query = categories.update().where(categories.c.id == id).values(**values)
        await self.database.execute(query=query)
        return category

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Category]:
        query = categories.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = categories.delete().where(categories.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Category]:
        query = categories.select().where(categories.c.id == id)
        category = await self.database.fetch_one(query=query)
        if category is None:
            return None
        return Category.parse_obj(category)
