from sqlalchemy import Column, Integer, String

from wkseguros.config import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    access_level = Column(Integer, nullable=False)
