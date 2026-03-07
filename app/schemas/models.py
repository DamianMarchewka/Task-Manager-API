from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime

    model_config = {"from_attributes": True}