from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from wkseguros.config.database import Base


class AccessLevel(Base):
    __tablename__ = 'access_level'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    
    # access_level = relationship("access_level", back_populates="user")
