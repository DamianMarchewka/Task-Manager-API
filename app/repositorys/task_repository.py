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


def get_tasks(db: Session, offset: int, limit: int, status: Optional[TaskStatus], title: Optional[str],
               sort_by: Optional[str], order: Optional[str]) -> list[Task]:
    stmt = (select(Task))
    if status is not None:
        stmt = stmt.where(Task.status == status)
    if title:
        stmt = stmt.where(Task.title.ilike(f"%{title}%"))
    sort_mapping = {
        "id": Task.id,
        "title": Task.title,
        "status": Task.status,
        "created_at": Task.created_at
    }
    sort_column = sort_mapping.get(sort_by, Task.id)
    if order == "desc":
        stmt = stmt.order_by(sort_column.desc())
    else:
        stmt = stmt.order_by(sort_column.asc())
    stmt = stmt.offset(offset).limit(limit)
    result = db.execute(stmt)
    return result.scalars().all()
# TODO (quality): validate sort_by and order values explicitly


def update_task(db: Session, task: Task) -> Task:
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> Task:
    db.delete(task)
    db.commit()
    return task
