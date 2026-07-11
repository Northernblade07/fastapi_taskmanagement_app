from sqlalchemy import Column , Integer, String , Boolean
from sqlalchemy.orm import relationship
from app.utils.db import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id= Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean , default=False)