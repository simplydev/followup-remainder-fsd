from fastapi import APIRouter,Depends,Security
from src.api.user.service import UserService
from src.api.user.schems import UserCreateInput

from fastapi.security import HTTPBearer  # 👈 new imports
from src.application.utils import VerifyToken
from src.auth0.auth0_service import get_user_by_id

router = APIRouter()
auth = VerifyToken()
# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()  # 👈 new code


@router.get("/onboard")
async def onboard(auth_result: str = Security(auth.verify),token = Depends(token_auth_scheme)):
    print("auth_result is "+str(auth_result))
    print("token is "+token.credentials)
    user_data = get_user_by_id(auth_result['sub'],token.credentials)
    print("user data is "+user_data)
    return {"message": "Welcome to the User API"}

@router.get("/")
async def read_users(user_service : UserService = Depends()):
    users = user_service.get_users()
    return users

@router.post("/")
async def create_user(user_create_input: UserCreateInput, user_service :UserService = Depends()):
    user = user_service.create_user(user_create_input)
    return user