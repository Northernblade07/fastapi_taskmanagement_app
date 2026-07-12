from app.tasks.dtos import TaskSchema , TaskResponseSchema
from sqlalchemy.orm import Session
from app.tasks.models import TaskModel
from fastapi import HTTPException
def create_task(body:TaskSchema , db:Session): 
    data = body.model_dump()
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_all_tasks(db:Session):
    return db.query(TaskModel).all()


def get_task( task_id:int, db : Session):
    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(404 , detail="Task not found")
    return {
        "status":"success",
        "message":"task found successfully",
        "data":task
    }


def update_task(body:TaskSchema , task_id:int , db:Session):
    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(404 , detail="Task not found")
    
    # this below is if you want to update every field manually
    # task.title = body.title
    # task.description = body.description
    # task.is_completed = body.is_completed

    # otherwise use a for loop for updating every field like below

    for field , value in body.model_dump().items():
        setattr(task , field , value)

    db.add(task)
    db.commit()
    db.refresh(task)
    return {"status":"success" , "message":"task updated successfully" , "data":task}


def delete_task(task_id:int , db:Session):
    task = db.query(TaskModel).get(task_id)

    if not task :
        raise HTTPException(404 , detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"status":"success" , "message":"task deleted successfully"}