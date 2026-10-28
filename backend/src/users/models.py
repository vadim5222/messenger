from typing import List, Optional


from sqlalchemy import ForeignKey, String, Column

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, validates





class Base(DeclarativeBase):
    pass


# ------------------Модель пользователя
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(50))

    surname: Mapped[str] = mapped_column(String(50))

    username: Mapped[str] = mapped_column(String(50))

    age: Mapped[int]

    active: Mapped[bool] = mapped_column(default=True)

    hashed_password: Mapped[str]

    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))

    role: Mapped['Role'] = relationship(back_populates='users')
    
    @validates('age')
    def validate_age(self, key, age):
        if age <=12 and age >= 100:
            raise ValueError('Возраст должен быть в диапазоне от 0 до 100')
        return age


    def __repr__(self):
        return f"User(id={self.id}!r), name={self.username}!r, fullname={self.name}!r"

    
# --------------------------------------Модель ролей
class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(30))

    users: Mapped[List[User]] = relationship(back_populates='role')

    permissions: Mapped[List['Permissions']] = relationship(secondary='role_permissions', back_populates='roles')


class Permissions(Base):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(30))

    roles: Mapped[List[Role]] = relationship(secondary='role_permissions', back_populates='permissions')

class Role_Permission(Base):
    __tablename__ = 'role_permissions'
    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    permission_id: Mapped[int] = mapped_column(ForeignKey('permissions.id'))








    








