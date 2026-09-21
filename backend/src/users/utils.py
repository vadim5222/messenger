from sqlmodel import select
from sqlalchemy.orm import joinedload
from database import SessionDep
from users.models import Users, Role
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .exceptions import credential_exception
from dotenv import load_dotenv
from tokens.schemas import TokenData
from .models import Users
from roles.service import get_role
from permissions.service import get_permission
import jwt
from jwt.exceptions import InvalidTokenError
import os
load_dotenv()



oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='token'
)



SECRET_KEY = os.getenv('SECRET_KEY') 
ALGORITHM = os.getenv('ALGORITHM') 

async def get_user(username: str, session: SessionDep):
    query = select(Users).where(Users.username == username).options(joinedload(Users.role).selectinload(Role.permissions))
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: SessionDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credential_exception
    user = await get_user(username=token_data.username, session=session)
    if not user:
        raise credential_exception
    return user

async def get_active_current_user(current_user: Annotated[Users, Depends(get_current_user)]):
    if not current_user.active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incative user'
        )
    return current_user


async def get_current_user_role(token: Annotated[str, Depends(oauth2_scheme)], session:SessionDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_role = payload.get('role')
        if user_role is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='This user does not have a role'
            )
        token_data = TokenData(role=user_role)
    except InvalidTokenError:
        raise credential_exception
    role = await get_role(title=token_data.role, session=session)
    if not role:
        raise credential_exception
    return role


async def get_current_user_permissions(token: Annotated[str, Depends(oauth2_scheme)], session: SessionDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_permissions = payload.get('permissions')
        if user_permissions is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='This user does not have a permissions'
            )
        token_data = TokenData(permissions=user_permissions)
    except InvalidTokenError:
        raise credential_exception
    permissions = await get_permission(titles=token_data.permissions, session=session)
    if not permissions:
        raise credential_exception
    return permissions
