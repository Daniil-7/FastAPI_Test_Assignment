from fastapi import Depends, HTTPException, status
from repositories.users import UserRepository
from repositories.jobs import JobRepository
from repositories.products import ProductRepository
from repositories.categories import CategoryRepository
from db.base import database
from core.security import JWTBearer, decode_access_token
from models.user import User

def get_user_repository() -> UserRepository:
    return UserRepository(database)

def get_job_repository() -> JobRepository:
    return JobRepository(database)

def get_product_repository() -> ProductRepository:
    return ProductRepository(database)

def get_category_repository() -> CategoryRepository:
    return CategoryRepository(database)


async def get_current_user(
    users: UserRepository = Depends(get_user_repository),
    token: str = Depends(JWTBearer()),
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user


