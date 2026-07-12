from app.user.dtos import UserSchema , UserLoginSchema
from sqlalchemy.orm import Session
from app.user.models import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash
import jwt
from app.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def get_hash_password(password):
    return password_hash.hash(password)

def register(body:UserSchema , db:Session):
    is_user_exist = db.query(UserModel).filter(UserModel.email == body.email).first()

    if is_user_exist:
        raise HTTPException(400 , detail="User already exist")
    

    hashed_password = get_hash_password(body.password)
    print(hashed_password)
    new_user = UserModel(
        username = body.username,
        email = body.email,
        hash_password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "status": "success" , 
        "message": "user registered successfully",
        "data":new_user
        }


def login(body:UserLoginSchema , db:Session):

    user = db.query(UserModel).filter(UserModel.email == body.email).first();
    if not user:
        raise HTTPException(404 , detail="User not found")
    
    if not password_hash.verify(body.password , user.hash_password):
        raise HTTPException(401 , detail="Invalid Credentails")

    exp_time = datetime.now() + timedelta(minutes = settings.EXP_TIME)
    token = jwt.encode({
        "user_id":user.id,
        "exp": exp_time
    } , settings.SECRET_KEY , algorithm=settings.ALGORITHM)
    return {
        "token":token
        }


