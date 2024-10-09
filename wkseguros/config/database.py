import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url db
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')

# Engine
engine = create_engine(DATABASE_URL, connect_args={'check_same_tread': False})

# Sessão de conexão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base para modelos
Base = declarative_base()
