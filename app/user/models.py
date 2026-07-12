from sqlalchemy import Column , Integer , String , Boolean , DateTime
from app.utils.db import Base


class UserModel(Base):
    __tablename__ = "user_table"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String)
    email = Column(String)
    hash_password = Column(String)
    created_at = Column(DateTime , default=True)


