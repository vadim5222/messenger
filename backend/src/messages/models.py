
from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime

from database import Base


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship





class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped["User"] = relationship(back_populates='messages')

    content: Mapped[str] = mapped_column(String(500))

    created_at: Mapped[datetime] = mapped_column(DateTime)

