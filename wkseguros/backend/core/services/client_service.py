from sqlalchemy.orm import session

from wkseguros.backend.models.client import Client
from wkseguros.backend.repositories.client_repository import ClientRepository
from wkseguros.backend.schemas.client import ClientCreate, ClientUpdate


class ClientService:
    def __init__(self, db: session):
        self.db = db
        self.client_respotiory = ClientRepository(db)

    def create_client(self, client_create: ClientCreate) -> Client:
        client = Client(**client_create.model_dump())
        return self.client_respotiory.create_client(client)

    def update_client(self, client_id: int, client_update: ClientUpdate) -> Client:
        client = self.client_respotiory.get_client_by_id(client_id)
        if not client:
            raise ValueError(f'Client com ID {client_id} não encontrado.')
        for key, value in client_update.model_dump(exclude_unset=True).items():
            setattr(client, key, value)
        return self.client_respotiory.update_client(client)

    def delete_client(self, client_id: int) -> None:
        Client = self.client_respotiory.get_client_by_id(client_id)
        if not Client:
            raise ValueError(f'Cliente com ID {client_id} não encontrado.')
        return self.client_respotiory.delete_client(client_id)

    def get_client_id(self, client_id: int) -> Client:
        client = self.client_respotiory.get_client_by_id(client_id)
        if not client:
            raise ValueError(f'Cliente com ID {client_id} não encontrado.')
        return client

    def get_all_clients(self) -> list[Client]:
        return self.client_respotiory.get_all_clients()
