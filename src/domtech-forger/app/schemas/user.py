import uuid
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, example="José da Silva")
    email: EmailStr = Field(..., example="jose.silva@email.com")
    password: str = Field(..., min_length=8, example="senhaSegura123")

class UserResponse(BaseModel):
    user_id: uuid.UUID
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str