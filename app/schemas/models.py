from pydantic import BaseModel, ConfigDict
from enum import Enum
from datetime import datetime
from typing import Optional

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

class TaskResponse(TaskBase):
    id: int
    status: TaskStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    