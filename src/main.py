from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from src.api.user.router import router as user_router
from src.api.todo.todo import router as todo_router

from fastapi import Depends, FastAPI  # 👈 new imports
from fastapi.security import HTTPBearer  # 👈 new imports
from src.application.utils import VerifyToken

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()  # 👈 new code



app = FastAPI()
auth = VerifyToken() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4040","*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(todo_router, prefix="/todo", tags=["todo"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

# new code 👇
@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    """A valid access token is required to access this route"""
    print("auth_result is "+str(auth_result))
    return auth_result
