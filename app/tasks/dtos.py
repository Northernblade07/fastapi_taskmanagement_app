from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    


class TaskOutSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id:int

class TaskResponseSchema(BaseModel):
    status:str
    message:str
    data:TaskOutSchema
  
  