from fastapi import APIRouter
from .schemas import RoleCreate
from database import SessionDep
from .service import create_role
from typing import Annotated
from users.models import Role
from fastapi import Depends
from users.utils import get_current_user_role

role_router = APIRouter()

@role_router.post('/roles')
async def create_new_role(title: RoleCreate, session: SessionDep):
    return await create_role(role=title, session=session)

@role_router.get('/roles/me')
async def get_current_user_role(current_role: Annotated[str, Depends(get_current_user_role)]):
    return current_role