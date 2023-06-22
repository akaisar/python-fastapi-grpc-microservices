from fastapi import Header
from app.interservice.auth import check_auth_token

async def check_authic_auth_token(
    x_authic_auth: str | None = Header(default=None),
) -> str | None:
    return check_auth_token(auth_token=x_authic_auth)
