from fastapi import APIRouter
from app.apps.auth.router.public_api import router as auth_router 
from app.apps.user.router.public_api import router as user_router 

from app.api.api_v1.endpoints import items, login, users, utils

api_router = APIRouter()
api_router.include_router(auth_router.router, tags=["login"])
api_router.include_router(user_router.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
