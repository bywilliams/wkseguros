from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import session
from wkseguros.backend.core.services.client_service import ClientService
from wkseguros.backend.schemas.client import ClientCreate, ClientUpdate, ClientResponse
from wkseguros.backend.utils.dependencies import get_db

router = APIRouter()

@router.get('/', response_model=list[ClientResponse])
def get_all_clients(db: session = Depends(get_db)):
    client_service = ClientService(db)
    return client_service.get_all_clients()