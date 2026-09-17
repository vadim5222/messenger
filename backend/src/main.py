from fastapi import FastAPI
from database import database_router
from auth.router import auth_router
from users.router import user_router
from roles.router import role_router
from permissions.router import permission_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(database_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(permission_router)


origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)