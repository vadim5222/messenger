from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(
        title='Имя',
        description='Введите ваше имя',
        min_length=0,
        max_length=100
    )

    surname: str = Field(
        title='Фамилия',
        description='Введите вашу фамилию',
        min_length=0,
        max_length=30
    ) 

    username: str | None = Field(
        title='Никнейм',
        description='Введите ваш никнейм',
        min_length=0,
        max_length=50
    ) 

    age: int = Field(
        title='Возраст',
        description='Введите ваш возраст',
        gt=12,
        lt=100
    )

    password: str = Field(
        title='Пароль',
        description='Введите ваш пароль',
        min_length=8,
        max_length=30
    )


class UserPublic(BaseModel):
    id: int
    
    name: str

    surname: str

    username: str

    age: int

    active: bool

    hashed_password: str