from sqlalchemy.orm import session

from wkseguros.backend.models.client import Client


class ClientRepository:
    def __init__(self, db: session):
        self.db = db

    def get_all_clients(self) -> list[Client]:
        """
        Returns a list of all clients.

        Returns:
        --------
        list[Client]
            A list of all client model instances.
        """
        return self.db.query(Client).all()

    def get_client_by_id(self, client_id: int) -> Client:
        """
        Retrieves a client by their ID.

        Parameters:
        -----------
        client_id : int
            The ID of the client to retrieve.

        Returns:
        --------
        Client
            The retrieved client model instance, or None if not found.
        """
        return self.db.query(Client).filter(Client.id == client_id).first()

    def create_client(self, client: Client) -> Client:
        """Create a client

        Args:
            client (Client): Client model

        Returns:
            Client: The retrieve client model instance, of None if  not found.
        """
        self.db.add(client)
        self.db.commit()
        self.db.refresh()
        return client

    def update_client(self, client: Client) -> Client:
        """Update a client

        Args:
            client (Client): client model instance

        Returns:
            Client: The retrieve client model instance, of None if not found.
        """
        self.db.merge(Client)
        self.db.commit()
        self.db.refresh(Client)
        return client

    def delete_client(self, client_id: int) -> None:
        """Delete a client

        Args:
            client_id (int): the client id
        """
        client = self.db.query(Client).filter(Client.id == client_id).first()
        if client:
            self.db.delete(client)
            self.db.commit()
