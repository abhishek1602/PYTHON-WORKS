from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud.user import get_user, create_user, update_user, get_user_history

router = APIRouter()

@router.post("/users/", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(session.get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(session.get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=UserRead)
def update_user_info(user_id: int, user: UserUpdate, db: Session = Depends(session.get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db=db, user_id=user_id, user=user)

@router.get("/users/{user_id}/history", response_model=list)
def read_user_history(user_id: int, db: Session = Depends(session.get_db)):
    return get_user_history(db=db, user_id=user_id)