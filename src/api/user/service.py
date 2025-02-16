from fastapi import Depends
from src.database import get_session
from src.api.user.models import User
from sqlmodel import  select, Session


class UserService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get_users(self):
        statement = select(User)
        users = self.session.exec(statement).all()
        return users
    
    def create_user(self, user_create_input):
        user = User(**user_create_input.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

