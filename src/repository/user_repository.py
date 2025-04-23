from typing import Sequence

from sqlmodel import Session, select
from src.model.user_model import User

def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def get_users(session: Session, skip: int = 0, limit: int = 10) -> Sequence[User] | None:
    return session.exec(select(User).offset(skip).limit(limit)).all()