import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from dotenv import load_dotenv
from fastapi import Depends
load_dotenv()
from typing import Annotated
from fastapi import APIRouter
from users.models import Users

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
        await conn.run_sync(Users.metadata.drop_all)
        await conn.run_sync(Users.metadata.create_all)
    return {'message':'Успех'}