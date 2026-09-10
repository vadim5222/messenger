from sqlmodel import SQLModel, Field


class User(SQLModel):
    username: str
    surname: str
    age: int

class Users(User, table=True):
    id: int = Field(primary_key=True)
    hashed_password: str

class UserCreate(User):
    password: str

class UserPublic(User):
    id: int



