from fastapi import APIRouter, HTTPException
from app.models.user_model import User, UserCreate
from app.services.user_service import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_all_users():
    return get_users()

@router.get("/{user_id}")
def get_user(user_id: int):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.post("/")
def add_user(user: UserCreate):
    return create_user(user)

@router.put("/{user_id}")
def edit_user(
    user_id: int,
    user: User
):

    updated = update_user(
        user_id,
        user
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated

@router.delete("/{user_id}")
def remove_user(user_id: int):
    return delete_user(user_id)