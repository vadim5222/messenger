from users.models import UserCreate, Users
from .utils import get_user
from security import verify_password
from dotenv import load_dotenv
from database import SessionDep
import os
load_dotenv()

DUMMY_HASH = os.getenv('DUMMY_HASH')


async def authenticate(session: SessionDep, username: str, password: str):
    user = await get_user(username=username, session=session)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
