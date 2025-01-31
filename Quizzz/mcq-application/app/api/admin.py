from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas import mcq as mcq_schemas, user as user_schemas
from app.crud import mcq as mcq_crud, user as user_crud
from app.core.security import get_current_user, AdminUser

router = APIRouter()

@router.post("/upload_mcq_bulk", response_model=str)
async def upload_mcq_bulk(mcqs: list[mcq_schemas.MCQCreate], current_user: AdminUser = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    mcq_crud.create_bulk(mcqs)
    return "MCQs uploaded successfully"

@router.get("/manage_users", response_model=list[user_schemas.User])
async def manage_users(current_user: AdminUser = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user_crud.get_all_users()

@router.delete("/delete_user/{user_id}", response_model=str)
async def delete_user(user_id: int, current_user: AdminUser = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    user_crud.delete_user(user_id)
    return "User deleted successfully"

@router.put("/update_user/{user_id}", response_model=str)
async def update_user(user_id: int, user_data: user_schemas.UserUpdate, current_user: AdminUser = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    user_crud.update_user(user_id, user_data)
    return "User updated successfully"