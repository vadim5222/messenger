from pydantic import BaseModel, Field

class RoleCreate(BaseModel):
    title: str | None = Field(
        title='Название роли',
        description='Введите название роли',
        min_length=0,
        max_length=20
    )

class RolePublic(RoleCreate):
    id: int

