from fastapi import FastAPI

from wkseguros.backend.api.V1 import router as api_v1_router
from wkseguros.config.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_v1_router, prefix='/api/v1')
