from fastapi import APIRouter , Depends
from app.user import controller
from app.utils.db import get_db
from app.user.dtos import UserSchema    

user_routes = APIRouter(prefix="/user" , tags=["User"])

@user_routes.post("/register" , status_code=201)
def register_user(body:UserSchema , db = Depends(get_db)):
    return controller.register(body , db)




@user_routes.post("/login" , status_code=201)
def login_user(body , db = Depends(get_db)):
    return controller.login(body , db)

