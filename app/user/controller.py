from app.user.dtos import UserSchema , UserLoginSchema
from sqlalchemy.orm import Session
from app.user.models import UserModel
from fastapi import HTTPException , Request
from pwdlib import PasswordHash
import jwt
from app.utils.settings import settings
from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError

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
        "exp": exp_time.timestamp()
    } , settings.SECRET_KEY , algorithm=settings.ALGORITHM)
    return {
        "token":token
        }


def is_authenticated(request:Request , db:Session):

    try :
        print(request.headers)
        token = request.headers.get("Authorization")
   
        if not token:
            raise HTTPException(401 , detail="Token not found")
        
        token = token.split(" ")[1]
        print(token)
        data = jwt.decode(token , settings.SECRET_KEY , algorithms=settings.ALGORITHM)
        user_id = data.get("user_id")
        exp_time = data.get("exp")

        current_time = datetime.now().timestamp()
        if current_time > exp_time:
            raise HTTPException(401 , detail="Token Expired")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(401 , detail="Invalid Credentails")


        return user
    except InvalidTokenError:
        raise HTTPException(401 , detail="Invalid Credentails")