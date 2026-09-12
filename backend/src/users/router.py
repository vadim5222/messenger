from fastapi import APIRouter, Depends
from typing import Annotated
from users.utils import get_current_user
from users.models import Users, UserPublic


user_router = APIRouter()

@user_router.get('/users/me', response_model=UserPublic)
async def read_users_me(current_user: Annotated[Users, Depends(get_current_user)]):
    return current_user