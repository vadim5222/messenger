from sqlmodel import SQLModel

class PermissionBase(SQLModel):
    title: str

class PermissionCreate(PermissionBase):
    title: str