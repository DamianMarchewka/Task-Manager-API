from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositorys import task_repository
from app.models.task import Task
from app.schemas.models import TaskCreate, TaskStatus


def get_task_by_id(db: Session, task_id: int) -> Task:
    task = task_repository.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
            )
    return task


def create_task(db: Session, task_create: TaskCreate) -> Task:
    task = Task(
        title=task_create.title,
        description=task_create.description,
        status=TaskStatus.todo
        )
    return task_repository.create_task(db, task)


def get_tasks(db: Session, skip: int = 0, limit: int = 20):
    if limit > 100:
        limit = 100
    if skip < 0:
        skip = 0
    return task_repository.get_tasks(db, skip=skip, limit=limit)