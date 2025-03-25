
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBaseSchema(BaseModel):
    username: str = Field(None, min_length=2, max_length=50)
    email: EmailStr
    first_name: str = Field(None, min_length=2, max_length=50)
    last_name: str = Field(None, min_length=2, max_length=50)
    created_at: datetime
    updated_at: datetime
    is_active: bool


class OptionalUserBaseSchema(BaseModel):
    username: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: Optional[bool] = None
