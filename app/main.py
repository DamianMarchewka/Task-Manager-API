from fastapi import FastAPI
from app.routers.tasks_router import router as task_router
from app.database.config import Base, engine

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "task-manager-api",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}


app.include_router(task_router)

Base.metadata.create_all(bind=engine)