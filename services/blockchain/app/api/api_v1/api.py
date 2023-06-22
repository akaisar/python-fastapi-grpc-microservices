from fastapi import APIRouter
from app import blockchain_rest

router = APIRouter(prefix="/blockchain/api")

router.include_router(
    blockchain_rest.router, prefix="", tags=["blockchain"]
)
