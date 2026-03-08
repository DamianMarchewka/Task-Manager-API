from fastapi import FastAPI
from app.routers.tasks_router import router as task_router
from app.database.config import Base, engine

app = FastAPI()

app.include_router(task_router)

Base.metadata.create_all(bind=engine)