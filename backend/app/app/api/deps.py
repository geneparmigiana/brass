from typing import Generator, AsyncGenerator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.apps.auth.schemas import AuthTokenPayload
from app.apps.user.models import User
from app.apps.user.dao import UserDAO
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from app.db.session import async_session

# explain the code below
"""
Code explanation: 
1. OAuth2PasswordBearer is a fastapi class that creates a dependency
2. reusable_oauth2 is an instance of OAuth2PasswordBearer
3. get_db is a dependency that creates a new database session and closes it after the request is finished
4. async_get_db is a dependency that creates a new async database session and closes it after the request is finished
5. get_current_user is a dependency that gets the current user from the database
6. get_current_active_user is a dependency that gets the current active user from the database
7. get_current_active_superuser is a dependency that gets the current active superuser from the database

"""
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def async_get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def get_current_user(
        db: AsyncSession = Depends(async_get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = AuthTokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await UserDAO.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
        current_user: User= Depends(get_current_user),
) -> User:
    if not UserDAO.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
        current_user: User = Depends(get_current_user),
) -> User:
    if not UserDAO.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
