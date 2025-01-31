from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserLogin, UserResponse
from app.core.security import verify_password, create_access_token
from app.crud.user import get_user_by_username

router = APIRouter()

@router.post("/login", response_model=UserResponse)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_login.username)
    if not user or not verify_password(user_login.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"username": user.username, "role": user.role, "access_token": access_token}

@router.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_active_user)):
    return current_user

def get_current_active_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    user = get_user_by_username(db, username)
    if user is None:
        raise credentials_exception
    return user