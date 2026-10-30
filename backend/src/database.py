import os
from dotenv import load_dotenv
from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession



from fastapi import Depends
from fastapi import APIRouter

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from users.models import (
    User,
    Permissions,
    Role,
    Role_Permission
)


from messages.models import (
    Message
)


load_dotenv()
database_router = APIRouter()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]



@database_router.post('/setup-database')
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {'message':'Успех'}