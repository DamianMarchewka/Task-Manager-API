from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.models import TaskStatus
from typing import Optional


def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    stmt = select(Task).where(Task.id == task_id)
    return db.scalars(stmt).first()


def get_tasks(db: Session, offset: int, limit: int, status: Optional[TaskStatus], title: Optional[str]) -> list[Task]:
    stmt = (select(Task).order_by(Task.id))
    if status is not None:
        stmt = stmt.where(Task.status == status)
    if title:
        stmt = stmt.where(Task.title.ilike(f"%{title}%"))
    stmt = stmt.offset(offset).limit(limit)
    result = db.execute(stmt)
    return result.scalars().all()


def update_task(db: Session, task: Task) -> Task:
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> Task:
    db.delete(task)
    db.commit()
    return task
