from sqlalchemy import Column , Integer, String , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from app.utils.db import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id= Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean , default=False)

    user_id = Column(Integer , ForeignKey("user_table.id" , ondelete="CASCADE"))