from fastapi import FastAPI
from app.utils.db import get_db , engine , Base
from app.tasks.models import TaskModel
from app.tasks.router import task_routes

Base.metadata.create_all(engine)

app = FastAPI(title="task_managemnet_app", version="1.0.0")

app.include_router(task_routes, prefix="/api/v1", tags=["Tasks"])
@app.get("/")
def root():
    return {"message": "Hello World"}
