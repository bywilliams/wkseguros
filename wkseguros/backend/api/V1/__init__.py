from fastapi import APIRouter

from .auth.auth import router as auth_router
from .client import router as client_router

router = APIRouter()
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(client_router, prefix='/clients', tags=['clients'])
