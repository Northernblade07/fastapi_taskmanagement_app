from fastapi import APIRouter , Depends
from app.tasks import controller
from app.tasks.dtos import TaskSchema
from app.utils.db import get_db

task_routes = APIRouter(prefix="/tasks" , tags=["Tasks"])

@task_routes.post("/create")
def create_task(body: TaskSchema , db = Depends(get_db)):
    return controller.create_task(body , db)

@task_routes.get("/all")
def get_all_tasks(db = Depends(get_db)):
    tasks =  controller.get_all_tasks(db)
    return {
        "status":"success",
        "data":tasks
    }

@task_routes.get("/{task_id}")
def get_tasks( task_id:int, db = Depends(get_db)):
    task = controller.get_task(task_id, db)
    return task


@task_routes.put("/update/{task_id}")
def update_task(body:TaskSchema , task_id:int , db = Depends(get_db)):
    return controller.update_task(body , task_id , db)


@task_routes.delete("/delete/{task_id}")
def delete_task(task_id:int , db = Depends(get_db)):
    return controller.delete_task(task_id , db)