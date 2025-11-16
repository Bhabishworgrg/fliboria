from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class Chat(SQLModel, table=True):
    id: int = Field(primary_key=True) 
    message: str = Field(max_length=255)
    time_stamp: datetime = Field(default_factory=datetime.utcnow)

    user_id: UUID = Field(foreign_key='user.id')
