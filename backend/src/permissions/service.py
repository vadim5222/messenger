from database import SessionDep
from users.models import Permission, Role
from sqlmodel import select
from .schemas import PermissionCreate
from fastapi import HTTPException, status

async def get_permission(title: str, session: SessionDep):
    query = select(Permission).where(Permission.title == title)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def create_permission(permission: PermissionCreate, session: SessionDep):
    exist_permission = await get_permission(title=permission.title, session=session)
    if exist_permission:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This permission already exist'
        )
    new_permission = Permission(
        title = permission.title
    )
    session.add(new_permission)
    await session.commit()
    await session.refresh(new_permission)
    return new_permission