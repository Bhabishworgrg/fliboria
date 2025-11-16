from sqlmodel import SQLModel, Field
from uuid import UUID


class Player(SQLModel, table=True):
    id: int = Field(primary_key=True) 
    user_name: str = Field(unique=True, max_length=255)
    skin_colour: int = Field()
    fin_colour: int = Field()

    user_id: UUID = Field(foreign_key='user.id')
