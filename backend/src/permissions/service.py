from database import SessionDep
from fastapi import HTTPException, status
from sqlmodel import select
from users.models import Permissions

from .schemas import PermissionCreate


async def get_permission(titles: list[str], session: SessionDep):
    query = select(Permissions).where(Permissions.title.in_(titles))
    result = await session.execute(query)
    return result.scalars().all()


async def create_permission(permission: PermissionCreate, session: SessionDep):
    exist_permission = await get_permission(titles=[permission.title], session=session)
    if exist_permission:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This permission already exist",
        )
    new_permission = Permissions(title=permission.title)
    session.add(new_permission)
    await session.commit()
    await session.refresh(new_permission)
    return new_permission
