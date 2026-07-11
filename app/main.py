from fastapi import FastAPI
from app.utils.db import get_db , engine , Base

Base.metadata.create_all(engine)

app = FastAPI(title="task_managemnet_app", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello World"}
