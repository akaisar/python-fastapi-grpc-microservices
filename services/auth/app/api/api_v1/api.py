from fastapi import APIRouter
from app import auth_rest

router = APIRouter(prefix="/auth/api")

router.include_router(
    auth_rest.router, prefix="", tags=["auth"]
)
