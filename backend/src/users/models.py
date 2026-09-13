from sqlmodel import SQLModel, Field, Relationship, Table
from typing import Optional, List



class User(SQLModel):
    username: str
    surname: str
    age: int
    active: bool 


class Users(User, table=True):
    id: int = Field(primary_key=True)
    hashed_password: str
    role_id: int = Field(foreign_key='role.id')
    roles:List["Role"] = Relationship(back_populates='users')

class UserCreate(User):
    password: str

class UserPublic(User):
    id: int


# ==============модели пользователя для прав доступа
class Role(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    permissions: List["Permission"] = Relationship(back_populates='roles')
    users: List[Users] = Relationship(back_populates='roles')

class Permission(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    role_id: int | None = Field(default=None, foreign_key='role.id')
    roles: Optional[Role] = Relationship(back_populates='permissions')


