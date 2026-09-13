from sqlmodel import SQLModel

class RoleBase(SQLModel):
    title: str


class RoleCreate(RoleBase):
    pass

