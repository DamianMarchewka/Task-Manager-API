from pydantic import BaseModel
from enum import Enum


class TaskStatus(str, Enum):
    todo = 'todo'
    in_progerss = 'in_progerss'
    dome = 'dome'

class TaskBase(BaseModel):
    title: str
    description: str
    status: TaskStatus

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None

class TaskResponse(TaskBase):
    id: int
    created_at: str
    status: TaskStatus | None = None

