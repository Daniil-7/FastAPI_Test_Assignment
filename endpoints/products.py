from typing import List
from models.products import Product, ProductIn
from models.user import User
from repositories.products import ProductRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_product_repository, get_current_user
from .errors import *
from db.categories import categories
from db.base import database

router = APIRouter()


@router.get("/", response_model=List[Product])
async def read_products(
    limit: int = 100,
    skip: int = 0,
    products: ProductRepository = Depends(get_product_repository),
):
    return await products.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Product)
async def create_product(
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    query = categories.select().where(categories.c.id == p.category_id)
    category_product = await database.fetch_one(query)
    check_product_id_category(category_product)
    return await products.create(p=p)


@router.put("/", response_model=Product)
async def update_product(
    id: int,
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    product = await products.get_by_id(id=id)
    check_404(product)
    query = categories.select().where(categories.c.id == p.category_id)
    category_product = await database.fetch_one(query)
    check_product_id_category(category_product)
    return await products.update(id=id, p=p)


@router.delete("/")
async def delete_product(
    id: int,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    product = await products.get_by_id(id=id)
    check_404(product)
    result = await products.delete(id=id)
    return {"status": True}
