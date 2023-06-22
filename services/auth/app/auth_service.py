from datetime import timedelta

from app.core.config import settings
from app.internals.user_writer import UserWriter
from app.internals.user_reader import UserReader
from app.core.security import verify_password, create_access_token

class AuthService:
    @staticmethod
    async def create_user(
        *,
        full_name: str,
        email: str,
        hashed_password: str,
    ) -> dict:
        await UserWriter.create(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password,
        )

    @staticmethod
    async def login(
        *,
        email: str,
        password: str,
    ) -> dict:
        user = await UserReader.get_user_by_email(
            email=email,
        )

        if not user:
            return None
        if not verify_password(plain_password=password, hashed_password=user['hashed_password']):
            return None

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {
            "access_token": create_access_token(
                user["id"], expires_delta=access_token_expires
            ),
            "token_type": "bearer",
        }
