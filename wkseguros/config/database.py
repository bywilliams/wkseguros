import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Obter o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto para o banco de dados
DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{os.path.abspath(os.path.join(BASE_DIR, "../wkseguros/app.db"))}')

# Engine
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

# Sessão de conexão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base para modelos
Base = declarative_base()
