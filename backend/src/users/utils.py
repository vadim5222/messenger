from sqlmodel import select
from database import SessionDep
from users.models import Users
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .exceptions import credential_exception
from dotenv import load_dotenv
from tokens.schemas import TokenData
import jwt
from jwt.exceptions import InvalidTokenError
import os
load_dotenv()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
SECRET_KEY = os.getenv('SECRET_KEY') 
ALGORITHM = os.getenv('ALGORITHM') 

async def get_user(username: str, session: SessionDep):
    query = select(Users).where(Users.username == username)
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
        
