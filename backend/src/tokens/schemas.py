from sqlmodel import SQLModel   

class Token(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenRead(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str

class RefreshToken(SQLModel):
    refresh_token: str


class TokenData(SQLModel):
    username: str | None = None
    role: str | None = None