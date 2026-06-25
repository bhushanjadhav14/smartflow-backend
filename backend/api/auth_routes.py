from backend.utils.auth_middleware import get_current_user
from fastapi import Depends

from fastapi import APIRouter, HTTPException

from backend.models.user_model import (
    UserRegister,
    UserLogin
)

from backend.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister):

    result = register_user(
        user.username,
        user.email,
        user.password
    )

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return result


@router.post("/login")
def login(user: UserLogin):

    result = login_user(
        user.email,
        user.password
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return result

@router.get("/auth/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "email": current_user["sub"]
    }