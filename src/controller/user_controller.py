from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.model.user_model import User
from src.database.database import get_session
import src.repository.user_repository as crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    return crud.create_user(session, user)


@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return crud.get_users(session, skip, limit)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = crud.get_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
