from sqlmodel import SQLModel, Field
from typing import Optional, List


class User(SQLModel):
    username: str
    surname: str
    age: int
    active: bool 
    role: Optional[List[str]] = None

class Users(User, table=True):
    id: int = Field(primary_key=True)
    hashed_password: str

class UserCreate(User):
    password: str

class UserPublic(User):
    id: int



