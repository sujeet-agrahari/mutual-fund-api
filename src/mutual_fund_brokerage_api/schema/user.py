from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('password')
    def password_validator(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        return v
    full_name: str
    is_active: bool = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None
    is_active: bool = True