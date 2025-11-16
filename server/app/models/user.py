from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    email: str = Field(unique=True, max_length=255)
    email_verified: bool = Field(default=False)
    password_hash: str = Field(max_length=255)
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    last_login: datetime | None = Field(default=None)
    is_banned: bool = Field(default=False)
