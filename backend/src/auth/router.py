from fastapi import APIRouter, HTTPException, status, Depends
from database import SessionDep
from users.models import UserCreate, Users, UserPublic
from security import get_password_hash
from users.utils import get_user
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from .exceptions import unauthorized_exception
from users.service import authenticate
from datetime import timedelta
from tokens.service import create_access_token
from tokens.schemas import TokenRead

auth_router = APIRouter()

@auth_router.post('/register', response_model=UserPublic)
async def register(session: SessionDep, user: UserCreate):
    exist_user = await get_user(username=user.username, session=session)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Такой пользователь уже существует'
        )
    new_user = Users(
        username = user.username,
        surname = user.surname,
        age = user.age,
        hashed_password = get_password_hash(user.password),
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@auth_router.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session:SessionDep):
    user = await authenticate(session=session, username=form_data.username, password=form_data.password)
    if not user:
        raise unauthorized_exception
    access_token_expire = timedelta(minutes=15)
    access_token = create_access_token(
        data={'sub': user.username},
        expire_delta=access_token_expire
    )
    return TokenRead(access_token=access_token, token_type='bearer')