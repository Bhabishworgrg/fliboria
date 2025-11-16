from fastapi import APIRouter

from app.crud.cruds import user_crud 
from app.core.deps import SessionDep
from app.schemas.user import UserRegister, UserCreate
from app.core.security import hash_password


router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/register')
def register_user(user: UserRegister, session: SessionDep):
    password_hash = hash_password(user.password)
    user_create = UserCreate(email=user.email, password_hash=password_hash)

    return user_crud.create(user_create, session)
