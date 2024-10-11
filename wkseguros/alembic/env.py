import os
import sys
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context

# Adicionando o caminho da pasta 'backend' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

# Importar a configuração do banco de dados e os modelos
from wkseguros.config.database import Base, DATABASE_URL

# Configuração do arquivo de log
fileConfig(context.config.config_file_name)

# Configuração do SQLAlchemy
config = context.config
config.set_main_option('sqlalchemy.url', DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()