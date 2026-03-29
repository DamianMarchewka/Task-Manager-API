from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositorys import task_repository
from app.models.task import Task
from app.schemas.models import TaskCreate, TaskStatus, TaskUpdate


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


def get_tasks(db: Session, skip: int, limit: int) -> list[Task]:
    return task_repository.get_tasks(db, skip=skip, limit=limit)


def update_task(db: Session, task_id: int, task_update: TaskUpdate) -> Task:
    task = get_task_by_id(db, task_id)
    update_data = task_update.model_dump(exclude_unset=True, exclude_none=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty data"
        )
    for key, value in update_data.items():
        setattr(task, key, value)
    return task_repository.update_task(db, task)


def delete_task(db: Session, task_id: int) -> None:
    task = get_task_by_id(db, task_id)
    task_repository.delete_task(db, task)
    return None