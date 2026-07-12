from sqlalchemy import Column , Integer , String , Boolean , DateTime , func
from app.utils.db import Base
from datetime import datetime , timezone

class UserModel(Base):
    __tablename__ = "user_table"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String)
    email = Column(String , index=True , unique=True)
    hash_password = Column(String)
    # created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    # or 
    created_at = Column(DateTime ,server_default=func.now())

