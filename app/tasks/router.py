from fastapi import APIRouter , Depends , status
from app.tasks import controller
from app.tasks.dtos import TaskSchema , TaskResponseSchema
from app.utils.db import get_db

task_routes = APIRouter(prefix="/tasks" , tags=["Tasks"])

@task_routes.post("/create",response_model=TaskResponseSchema , status_code=201)
def create_task(body: TaskSchema , db = Depends(get_db)):
    new_task = controller.create_task(body , db)
    return {"status":"success" , "message":"task created successfully" , "data":new_task}

@task_routes.get("/all" , status_code=status.HTTP_200_OK)
def get_all_tasks(db = Depends(get_db)):
    tasks =  controller.get_all_tasks(db)
    return {
        "status":"success",
        "message":"tasks found successfully",
        "data":tasks
    }

@task_routes.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_tasks( task_id:int, db = Depends(get_db)):
    task = controller.get_task(task_id, db)
    return task


@task_routes.put("/update/{task_id}", status_code=status.HTTP_200_OK)
def update_task(body:TaskSchema , task_id:int , db = Depends(get_db)):
    return controller.update_task(body , task_id , db)


@task_routes.delete("/delete/{task_id}" , status_code=status.HTTP_200_OK)
def delete_task(task_id:int , db = Depends(get_db)):
    return controller.delete_task(task_id , db)