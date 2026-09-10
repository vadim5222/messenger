from fastapi import APIRouter, Depends
from typing import Annotated
from users.utils import get_current_user
from users.models import Users


user_router = APIRouter()

@user_router.get('/users/me')
async def read_users_me(current_user: Annotated[Users, Depends(get_current_user)]):
    return current_user