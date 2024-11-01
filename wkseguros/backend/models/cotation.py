from datetime import datetime, timezone

from sqlalchemy import Column, Integer, Numeric, TIMESTAMP, String, Boolean, Date, DateTime

from wkseguros.config.database import Base


class Cotation(Base):
    __tablename__ = 'cotation'
    id = Column(Integer, primary_key=True, index=True)
    insurance_type = Column(Integer, nullable=False)
    cotation_date = Column(DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    validation_date = Column(DateTime, 
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    cotation_value = Column(Numeric(10,2), nullable=False)
    details = Column(String, nullable=True)
    status = Column(Integer, nullable=False)