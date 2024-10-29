from sqlalchemy.orm import Session

from wkseguros.backend.models.client import Client
from wkseguros.backend.repositories.client_repository import ClientRepository
from wkseguros.backend.schemas.client import ClientCreate, ClientUpdate, ClientResponse


class ClientService:
    def __init__(self, db: Session):
        self.db = db
        self.client_repository = ClientRepository(db)

    def create_client(self, client_create: ClientCreate) -> Client:
        client = Client(**client_create.model_dump())
        return self.client_repository.create_client(client)

    def update_client(self, client_id: int, client_update: ClientUpdate) -> Client:
        client = self.client_repository.get_client_by_id(client_id)
        for key, value in client_update.model_dump(exclude_unset=True).items():
            setattr(client, key, value)
        return self.client_repository.update_client(client)

    def delete_client(self, client_id: int) -> None:
        Client = self.client_repository.get_client_by_id(client_id)
        if not Client:
            raise ValueError(f'Cliente com ID {client_id} não encontrado.')
        return self.client_repository.delete_client(client_id)

    def get_client_id(self, client_id: int) -> Client:
        client = self.client_repository.get_client_by_id(client_id)
        if not client:
            raise ValueError(f'Cliente com ID {client_id} não encontrado.')
        return client
    
    def get_client_by_email(self, email: str) -> Client:
        return self.client_repository.get_client_by_email(email)
    
    def get_client_by_cpf(self, cpf: str) -> Client:
        return self.client_repository.get_client_by_cpf(cpf)

    def get_all_clients(self) -> list[ClientResponse]:
        clients = self.client_repository.get_all_clients()
        return [ClientResponse.model_validate(client) for client in clients]
