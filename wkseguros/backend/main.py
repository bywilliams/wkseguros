from fastapi import FastAPI

from wkseguros.backend.api.V1.auth import router as api_router_auth
from wkseguros.config.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router_auth, prefix="/api/v1")
