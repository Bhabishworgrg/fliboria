from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class Log(SQLModel, table=True):
    id: int = Field(primary_key=True) 
    time_stamp: datetime = Field(default_factory=datetime.utcnow)
    info: str = Field(max_length=255)

    user_id: UUID = Field(foreign_key='user.id')
