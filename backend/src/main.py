from fastapi import FastAPI
from database import database_router
from auth.router import auth_router
from users.router import user_router

app = FastAPI()

app.include_router(database_router)
app.include_router(auth_router)
app.include_router(user_router)