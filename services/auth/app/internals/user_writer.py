from typing import Optional

from models.user import UserModel
from app.internals.user_reader import UserReader

class UserWriter:
    @staticmethod
    async def create(
        *,
        full_name: str,
        email: str,
        hashed_password: str,
    ) -> dict:
        user = UserModel(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password,
        )
        await user.save()
        return await UserReader.get_user_by_id(id=user.id)
