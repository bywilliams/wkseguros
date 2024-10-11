from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime

from wkseguros.config import Base

class AccessLevel(Base):
    __tablename__ = "access_level"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))