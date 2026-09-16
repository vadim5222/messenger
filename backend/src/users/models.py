from sqlmodel import SQLModel, Field, Relationship
from typing import List



# ========================Модели ролей и разрешений

class RolePermissionLink(SQLModel, table=True):
    role_id: int | None = Field(default=None, foreign_key='role.id', primary_key=True)
    permission_id: int | None = Field(default=None, foreign_key='permission.id', primary_key=True)


class Role(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    users: List["Users"] = Relationship(back_populates='role')
    permissions: List["Permission"] = Relationship(back_populates='roles', link_model=RolePermissionLink)


class Permission(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    roles: List["Role"] = Relationship(back_populates='permissions', link_model=RolePermissionLink)



# ======================Модели пользователя
class User(SQLModel):
    username: str
    surname: str
    age: int
    active: bool 

class UserCreate(User):
    password: str

class UserPublic(User):
    id: int


class Users(User, table=True):
    id: int = Field(primary_key=True)
    role_id: int| None = Field(default=None, foreign_key='role.id')
    role: Role | None = Relationship(back_populates='users')
    hashed_password: str









