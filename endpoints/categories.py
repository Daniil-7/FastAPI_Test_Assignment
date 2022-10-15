from typing import List
from models.categories import Category, CategoryIn
from models.user import User
from repositories.categories import CategoryRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_category_repository, get_current_user

router = APIRouter()

@router.get("/", response_model=List[Category])
async def read_categories(
    limit: int = 100,
    skip: int = 0,
    categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Category)
async def create_category(
    c: CategoryIn, 
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to create a category")
    return await categories.create(c=c)

@router.put("/", response_model=Category)
async def update_category(
    id: int,
    c: CategoryIn, 
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to update a category")
    category = await categories.get_by_id(id=id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await categories.update(id=id, c=c)

@router.delete("/")
async def delete_category(id: int,
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user)):
    if not current_user.is_company:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough rights to delete a category")
    category = await category.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    if category is None:
        raise not_found_exception
    result = await categories.delete(id=id)
    return {"status": True}