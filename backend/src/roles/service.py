from database import SessionDep
from users.models import Role
from .schemas import RoleCreate
from sqlmodel import select
from fastapi import HTTPException, status


async def get_role(title: str, session: SessionDep):
    query = select(Role).where(Role.title == title)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def create_role(role: RoleCreate, session:SessionDep):
    exist_role = await get_role(title=role.title, session=session)
    if exist_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This role already exist'
        )
    new_role = Role(
        title = role.title
    )
    session.add(new_role)
    await session.commit()
    await session.refresh(new_role)
    return new_role
