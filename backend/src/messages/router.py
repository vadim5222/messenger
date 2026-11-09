from typing import Annotated

from fastapi import APIRouter, Depends



from .schemas import MessageCreate, MessagePublic


from database import SessionDep


from .models import Message


from users.models import User
from users.utils import get_active_current_user

from sqlalchemy import select


message_route = APIRouter()


@message_route.post('/message/', response_model=MessagePublic)
async def send_message(session: SessionDep, message: MessageCreate):
    new_message = Message(
        sender_id = message.sender_id,
        recipient_id = message.recipient_id,
        content = message.content,
        created_at = message.created_at
    )
    session.add(new_message)
    await session.commit()
    await session.refresh(new_message)
    return new_message


@message_route.get('/message/', response_model=list[MessagePublic])
async def get_my_message(session: SessionDep, current_user: Annotated[User, Depends(get_active_current_user)]):
    query = select(Message).where(Message.recipient_id == current_user.id)
    result = await session.execute(query)
    return result.scalars().all()