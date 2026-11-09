
from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String, DateTime

from database import Base


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship





class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)

    sender_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    recipient_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


    sender = relationship("User", foreign_keys=[sender_id], back_populates='sent_messages')

    recipient = relationship("User", foreign_keys=[recipient_id], back_populates='received_messages')

    content: Mapped[str] = mapped_column(String(500))

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))

