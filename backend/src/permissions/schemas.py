from pydantic import BaseModel, Field

class PermissionCreate(BaseModel):
    title: str = Field(
        title='Разрешение',
        description='Введите название разрешения',
        min_length=0,
        max_length=20
    )

class PermissionPublic(PermissionCreate):
    id: int