from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import Task


def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    stmt = select(Task).where(Task.id == task_id)
    return db.scalars(stmt).first()


def get_tasks(db: Session, skip: int, limit: int) -> list[Task]:
    stmt = (select(Task).order_by(Task.id).offset(skip).limit(limit))
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
