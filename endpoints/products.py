from typing import List
from models.products import Product, ProductIn
from models.user import User
from repositories.products import ProductRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_product_repository, get_current_user

router = APIRouter()

@router.get("/", response_model=List[Product])
async def read_products(
    limit: int = 100,
    skip: int = 0,
    products: ProductRepository = Depends(get_product_repository)):
    return await products.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Product)
async def create_product(
    p: ProductIn, 
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to create a product")
    return await products.create(p=p)

@router.put("/", response_model=Product)
async def update_product(
    id: int,
    p: ProductIn, 
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to update a product")
    product = await products.get_by_id(id=id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return await products.update(id=id, p=p)

@router.delete("/")
async def delete_product(id: int,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to delete a product")
    product = await product.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    if job is None:
        raise not_found_exception
    result = await products.delete(id=id)
    return {"status": True}