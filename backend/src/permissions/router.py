from typing import Annotated


from fastapi import APIRouter, Depends

from database import SessionDep
from security import RoleChecker, UserRoles


from .schemas import PermissionCreate
from .service import create_permission


from users.utils import get_current_user_permissions


permission_router = APIRouter()


role_checker = RoleChecker(UserRoles.admin)



@permission_router.post('/permissions', dependencies=[Depends(role_checker)])
async def create_new_permission(permission: PermissionCreate, session: SessionDep):
    return await create_permission(permission=permission, session=session)


@permission_router.get('/permissions/me')
async def read_permissions_me(current_permissions: Annotated[list, Depends(get_current_user_permissions)]):
    return current_permissions