from fastapi import FastAPI

from wkseguros.backend.routes import auth
from wkseguros.config.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
