from typing import List, Any
from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserPayloadSchema, UserResponseSchema
from app.schemas.token import Token
from app.auth_service import AuthService
from app.core.security import get_password_hash

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def register(payload: UserPayloadSchema) -> UserResponseSchema:
    return await AuthService.create_user(
        full_name=payload.full_name,
        email=payload.email,
        hashed_password=get_password_hash(payload.password),
    )

@router.post("/login/access-token", response_model=Token)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return await AuthService.login(
        email=form_data.username,
        password=form_data.password,
    )
