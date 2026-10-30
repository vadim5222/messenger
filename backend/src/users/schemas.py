from typing import Annotated

from pydantic import BaseModel, Field, AfterValidator




def age_validator(value: int) -> int:
    if value < 12 or value > 100:
        raise ValueError(f'Ваш возраст - {value}. Возраст должен быть от 12 до 100 лет')
    return value


class UserBase(BaseModel):
    name: str = Field(
        title="Имя", description="Введите ваше имя", min_length=0, max_length=100
    )

    surname: str = Field(
        title="Фамилия", description="Введите вашу фамилию", min_length=0, max_length=30
    )

    username: str | None = Field(
        title="Никнейм", description="Введите ваш никнейм", min_length=0, max_length=50
    )

    age: Annotated[int, AfterValidator(age_validator)] = Field(
        title='Возраст',
        description='Введите ваш возраст'
    )


class UserCreate(UserBase):
    password: str = Field(
        title="Пароль", description="Введите ваш пароль", min_length=8, max_length=30
    )


class UserPublic(UserBase):
    id: int
    active: bool
