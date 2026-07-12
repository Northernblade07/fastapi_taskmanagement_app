from app.user.dtos import UserSchema
from sqlalchemy.orm import Session
from app.user.models import UserModel
def register(body:UserSchema , db:Session):
    new_user = UserModel(
        username = body.username,
        email = body.email,
        hash_password = body.password
    )
    return {
        "status": "success" , 
        "message": "user registered successfully"
        }


def login(body , db:Session):
    return {
        "status": "success" , 
        "message": "user logged in successfully"
        }


