#from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.apps.user.schemas import UserCreate
from app.apps.user.dao import UserDAO
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


async def init_db(db: AsyncSession) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    # explain the code below
    # if you want to create a superuser, you need to create a user first
    # but you can't create a user without a hashed password
    # so you need to create a user with a password, then update the user
    # with the hashed password
    # the code below does that


    user = await UserDAO.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            phone="88005553535",
            is_superuser=True,
        )
        user = await UserDAO.create(db, obj_in=user_in)  # noqa: F841
        user = await UserDAO.update(db, db_obj=user, obj_in={"is_active": True})  # noqa: F841
