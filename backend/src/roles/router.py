from fastapi import APIRouter
from .schemas import RoleCreate
from database import SessionDep
from .service import create_role

role_router = APIRouter()

@role_router.post('/roles')
async def create_new_role(title: RoleCreate, session: SessionDep):
    return await create_role(role=title, session=session)