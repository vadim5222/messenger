from fastapi import APIRouter
from .schemas import PermissionCreate
from database import SessionDep
from .service import create_permission

permission_router = APIRouter()

@permission_router.post('/permissions')
async def create_new_permission(permission: PermissionCreate, session: SessionDep):
    return await create_permission(permission=permission, session=session)