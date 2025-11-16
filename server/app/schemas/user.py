from pydantic import BaseModel


class UserRegister(BaseModel):
    user_name: str
    email: str
    password: str
    skin_color: int
    fin_color: int
    captcha_token: str 


class UserCreate(BaseModel):
    email: str
    password_hash: str
