from pydantic import BaseModel

class UserPayloadSchema(BaseModel):
    full_name: str
    email: str
    password: str

class UserResponseSchema(BaseModel):
    id: int
    full_name: str
    email: str
    hashed_password: str
