from datetime import datetime, timezone

from typing import List

from database import Base

from sqlalchemy import ForeignKey, String, DateTime


from sqlalchemy.orm import Mapped, mapped_column, relationship




class Chat(Base):
    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str]

    users: Mapped[List["User"]] = relationship(
        secondary='users_chats', back_populates='chats'
    )