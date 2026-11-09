from datetime import datetime, timezone

from pydantic import BaseModel, Field
from typing import Text

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: Text
    created_at: datetime = Field(
        default=datetime.now(timezone.utc)
    )

class MessagePublic(MessageCreate):
    pass 
    