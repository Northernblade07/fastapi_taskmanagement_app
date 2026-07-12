from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class RegisterResponse(BaseModel):
    id:int
    username:str
    email:str
    created_at: datetime


class UserReponseSchema(BaseModel):
    status: str
    message: str
    data: RegisterResponse


class UserLoginSchema(BaseModel):
    email: str
    password: str


