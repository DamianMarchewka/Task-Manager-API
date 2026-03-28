from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.models import TaskCreate, TaskResponse, TaskUpdate
from app.services import task_service


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


@router.get("/", response_model=list[TaskResponse])
def list_tasks(skip: int = Query(0, ge=0),
               limit: int = Query(20, le=100),
               db: Session = Depends(get_db)
):
    return task_service.get_tasks(db, skip=skip, limit=limit)


@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def task_update(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    return task_service.update_task(db, task_id, task_update)
