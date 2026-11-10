from fastapi import APIRouter, WebSocket

from database import SessionDep

from .schemas import ChatCreate, ChatPublic

from .models import Chat

from users.models import User

from sqlalchemy import select

from sqlalchemy.orm import lazyload

chat_router = APIRouter()


@chat_router.post('/chats/')
async def create_chat(session: SessionDep, chat: ChatCreate):
    query = select(User).where(User.id.in_(chat.users))
    result = await session.execute(query)
    users = result.scalars().all()

    new_chat = Chat(
        title = chat.title,
        users = users
    )

    session.add(new_chat)
    await session.commit()
    await session.refresh(new_chat)
    return new_chat


@chat_router.get('/chats/{id}')
async def get_users_in_chat(id: int, session: SessionDep):
    query = (select(User).join(User.chats).where(Chat.id == id))
    result = await session.execute(query)
    users = result.scalars().all()
    return users




@chat_router.websocket('/ws')
async def websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()