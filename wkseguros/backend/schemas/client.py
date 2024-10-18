from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    last_name: str
    cpf: str
    born_date: date | None = None
    address: str
    email: EmailStr
    phone: str
    
    class Config:
        # Define o formato da data ao exportar como JSON
        json_encoders = {
            date: lambda v: v.strftime('%d/%m/%Y')
        }


class ClientCreate(ClientBase):
    created_at: datetime


class ClientUpdate(ClientBase):
    name: str | None = None
    last_name: str | None = None
    cpf: str | None = None
    born_date: date | None = None
    address: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    updated_at: datetime | None = None


class ClientResponse(ClientCreate):
    id: int
    created_at: datetime
    updated_at: datetime

