from datetime import datetime, timezone

from sqlalchemy import Column, Date, DateTime, Integer, String

from wkseguros.config.database import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    born_date = Column(Date, nullable=True)
    address = Column(String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String(11), nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
