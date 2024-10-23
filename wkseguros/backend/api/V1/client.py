from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from sqlalchemy.orm import session
from wkseguros.backend.core.services.client_service import ClientService
from wkseguros.backend.schemas.client import ClientCreate, ClientUpdate, ClientResponse
from wkseguros.backend.utils.dependencies import get_db

router = APIRouter()

@router.get('/', response_model=list[ClientResponse])
def get_all_clients(db: session = Depends(get_db)):
    client_service = ClientService(db)
    return client_service.get_all_clients()

@router.post('/', response_model=ClientResponse)
def create_client(client_create: ClientCreate, db: session = Depends(get_db)):
    client_service = ClientService(db)
    try:
        new_client = client_service.create_client(client_create)
        return new_client
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put('/{client_id}', response_model=ClientResponse)
def update_client(client_id: int, client_update: ClientUpdate, db: session = Depends(get_db)):
    client_service = ClientService(db)
    try:
        if isinstance(client_update.born_date, str):
            client_update.born_date = datetime.strptime(client_update.born_date, '%Y-%m-%d')
        updated_client = client_service.update_client(client_id, client_update)
        return updated_client
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete('/{client_id}', response_model=None)
def delete_client(client_id: int, db: session = Depends(get_db)):
    client_service = ClientService(db)
    try:
        client_service.delete_client(client_id)
        return {"detail": "Cliente deletado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))