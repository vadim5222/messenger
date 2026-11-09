from typing import List
\
from pydantic import BaseModel, Field

class ChatCreate(BaseModel):
    title: str
    users: List[int] = Field(min_length=1)


class ChatPublic(ChatCreate):
    pass