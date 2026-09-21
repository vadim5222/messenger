from fastapi import APIRouter, Depends
from .schemas import PermissionCreate
from database import SessionDep
from .service import create_permission
from typing import Annotated
from users.utils import get_current_user_permissions

permission_router = APIRouter()

@permission_router.post('/permissions')
async def create_new_permission(permission: PermissionCreate, session: SessionDep):
    return await create_permission(permission=permission, session=session)


@permission_router.get('/permissions/me')
async def read_permissions_me(current_permissions: Annotated[list, Depends(get_current_user_permissions)]):
    return current_permissions