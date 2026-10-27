from pydantic import BaseModel 
from typing import List

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenRead(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class RefreshToken(BaseModel):
    refresh_token: str


class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None
    permissions: List[str] | None = None