from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.models import TaskCreate, TaskResponse, TaskUpdate, TaskStatus
from app.services import task_service
from typing import Optional


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
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
def list_tasks(status: Optional[TaskStatus] = Query(None),
               title: Optional[str] = Query(None),
               sort_by: Optional[str] = Query(None),
               order: Optional[str] = Query(None),
               offset: int = Query(0, ge=0),
               limit: int = Query(20, le=100),
               db: Session = Depends(get_db)
):
    return task_service.get_tasks(db, status=status, title=title, sort_by=sort_by, order=order, offset=offset, limit=limit)


@router.patch("/{task_id}", response_model=TaskResponse)
def task_update(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    return task_service.update_task(db, task_id, task_update)


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
    ) -> None:
    task_service.delete_task(db, task_id)