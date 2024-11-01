from sqlalchemy import Column, Integer, String

from wkseguros.config.database import Base


class Cotation(Base):
    __tablename__ = 'cotation_status'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)