from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.models import TaskCreate, TaskResponse
from app.services import task_service
from typing import List


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate, 
    db: Session = Depends(get_db)
    ):
    return task_service.create_task(db, task)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return task_service.get_task_by_id(db, task_id)


@router.get("/", response_model=List[TaskResponse])
def list_tasks(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return task_service.get_tasks(db, skip=skip, limit=limit)