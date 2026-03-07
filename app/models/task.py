from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime, timezone
from app.database.config_db import Base
from app.schemas.models import TaskStatus


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))