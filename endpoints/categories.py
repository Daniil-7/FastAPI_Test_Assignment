from typing import List
from models.categories import Category, CategoryIn
from models.user import User
from repositories.categories import CategoryRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_category_repository, get_current_user
from .errors import check_is_superuser, check_404

router = APIRouter()


@router.get("/", response_model=List[Category])
async def read_categories(
    limit: int = 100,
    skip: int = 0,
    categories: CategoryRepository = Depends(get_category_repository),
):
    return await categories.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Category)
async def create_category(
    c: CategoryIn,
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    return await categories.create(c=c)


@router.put("/", response_model=Category)
async def update_category(
    id: int,
    c: CategoryIn,
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    category = await categories.get_by_id(id=id)
    check_404(category)
    return await categories.update(id=id, c=c)


@router.delete("/")
async def delete_category(
    id: int,
    categories: CategoryRepository = Depends(get_category_repository),
    current_user: User = Depends(get_current_user),
):
    check_is_superuser(current_user)
    category = await category.get_by_id(id=id)
    check_404(category)
    result = await categories.delete(id=id)
    return {"status": True}
