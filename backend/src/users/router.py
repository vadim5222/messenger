from typing import Annotated, List

from database import SessionDep


from fastapi import APIRouter, Depends, HTTPException, status


from sqlalchemy import select


from security import UserRoles, RoleChecker, UserPermissions, PermissionChecker


from users.models import User
from users.schemas import UserPublic
from users.utils import get_active_current_user, get_user_by_id

user_router = APIRouter()

role_checker = RoleChecker([UserRoles.admin, UserRoles.user])
permission_checker = PermissionChecker(UserPermissions.user_delete)




@user_router.get("/users", response_model=List[UserPublic], dependencies=[Depends(role_checker)])
async def read_users(session: SessionDep, ):
    query = select(User)
    result = await session.execute(query)
    users = result.scalars().all()
    return users


@user_router.get("/users/me", response_model=UserPublic)
async def read_users_me(
    current_user: Annotated[User, Depends(get_active_current_user)],
):
    return current_user


@user_router.delete('/users/delete/{id}', dependencies=[Depends(permission_checker)])
async def delete_user(id: int, session:SessionDep):
    user = await get_user_by_id(user_id=id, session=session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )
    await session.delete(user)
    await session.commit()
    return {
        'access':'Пользователь успешно удален'
    }







