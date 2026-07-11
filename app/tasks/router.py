from fastapi import APIRouter , Depends
from app.tasks import controller
from app.tasks.dtos import TaskSchema
from app.utils.db import get_db

task_routes = APIRouter(prefix="/tasks" , tags=["Tasks"])

@task_routes.post("/create")
def create_task(body: TaskSchema , db = Depends(get_db)):
    return controller.create_task(body , db)