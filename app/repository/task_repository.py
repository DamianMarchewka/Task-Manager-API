from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()


# TODO dadać funkcje (get, update, delete)
# get_tasks
# update_task
# delete_task