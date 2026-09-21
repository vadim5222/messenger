from fastapi import APIRouter, HTTPException, status, Depends
from database import SessionDep
from users.models import UserCreate, Users, UserPublic, Role
from security import get_password_hash
from users.utils import get_user
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from .exceptions import unauthorized_exception
from users.exceptions import credential_exception
from users.service import authenticate
from datetime import timedelta
from tokens.service import create_access_token, create_refresh_token
from tokens.schemas import TokenRead, TokenData, RefreshToken
from .exceptions import unauthorized_exception
import jwt
from sqlmodel import select
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
load_dotenv()
import os



auth_router = APIRouter()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')



@auth_router.post('/register', response_model=UserPublic)
async def register(session: SessionDep, user: UserCreate):
    exist_user = await get_user(username=user.username, session=session)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Такой пользователь уже существует'
        )
    role_select = select(Role).where(Role.title == 'User')
    role_execute = await session.execute(role_select)
    role = role_execute.scalar_one_or_none()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Role is none'
        )
    new_user = Users(
        username = user.username,
        surname = user.surname,
        age = user.age,
        active=user.active,
        hashed_password = get_password_hash(user.password),
        role_id=role.id
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@auth_router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session:SessionDep):
    user = await authenticate(session=session, username=form_data.username, password=form_data.password)
    if not user:
        raise unauthorized_exception
    access_token_expire = timedelta(minutes=15)
    refresh_token_expire = timedelta(days=15)
    access_token = create_access_token(
        data={
            'sub': user.username,
            'role': user.role.title,
            'permissions': [p.title for p in user.role.permissions]
        },
        expire_delta=access_token_expire
    )
    refresh_token = create_refresh_token(
        data={'sub': user.username},
        expire_delta=refresh_token_expire
    )
    return TokenRead(access_token=access_token, refresh_token=refresh_token, token_type='bearer')

@auth_router.post('/refresh')
async def refresh(refresh_token: RefreshToken):
    try:
        payload = jwt.decode(refresh_token.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise unauthorized_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credential_exception
    new_access_expire_delta = timedelta(minutes=15)
    new_access_token = create_access_token(data={'sub': token_data.username}, expire_delta=new_access_expire_delta)
    return TokenRead(access_token=new_access_token, refresh_token=refresh_token.refresh_token, token_type='bearer')