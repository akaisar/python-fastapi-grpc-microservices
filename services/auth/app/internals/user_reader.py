from typing import Optional

from models.user import UserModel

class UserReader:
    @staticmethod
    async def get_user_by_id(
        *,
        id: int,
    ) -> Optional[dict]:
        user = await UserModel.filter(id=id).first().values()
        if user:
            return user[0]
        return None

    @staticmethod
    async def get_user_by_email(
        *,
        email: str,
    ) -> Optional[dict]:
        user = await UserModel.filter(email=email).first().values()
        if user:
            return user[0]
        return None
