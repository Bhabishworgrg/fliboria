from typing import List
from sqlmodel import Session, select, SQLModel
from pydantic import BaseModel


class BaseCRUD:
    model = None 

    def create(self, schema: BaseModel, session: Session) -> SQLModel:
        record = self.model(**schema.model_dump())

        session.add(record)
        session.commit()
        session.refresh(record)

        return record 

    def get(self, id: int | str, session: Session) -> SQLModel | None:
        query = select(self.model).where(self.model.id == id)
        return session.exec(query).first()

    def get_all(self, session: Session) -> List[SQLModel]:
        query = select(self.model)
        return session.exec(query).all()

    def update(self, id: int | str, schema: BaseModel, session: Session) -> SQLModel | None:
        record = self.get(id, session)
        if not record:
            return None

        for key, value in schema.model_dump(exclude_unset=True).items():
            setattr(record, key, value)

        session.add(record)
        session.commit()
        session.refresh(record)

        return record

    def delete(self, id: int | str, session: Session) -> bool:
        record = self.get(id, session)
        if not record:
            return False

        session.delete(record)
        session.commit()
        return True
