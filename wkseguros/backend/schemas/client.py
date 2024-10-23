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
        from_attributes = True
    
    # class Config:
    #     # Define o formato da data ao exportar como JSON
    #     json_encoders = {
    #         date: lambda v: v.strftime('%d/%m/%Y'),
    #         datetime: lambda v: v.strftime('%Y-%m-%dT%H:%M:%S')
    #     }


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
    updated_at: datetime
    formatted_born_date: str | None = None  # Campo para data formatada
    iso_born_date: str | None = None  # Campo para input de data
    formatted_created_at: str | None = None

    @classmethod
    def model_validate(cls, obj):
        instance = super().model_validate(obj)
        instance.formatted_created_at = obj.created_at.strftime('%d/%m/%Y %H:%M') if obj.created_at else None
        instance.formatted_born_date = obj.born_date.strftime('%d/%m/%Y') if obj.born_date else None
        instance.iso_born_date = obj.born_date.strftime('%Y-%m-%d') if obj.born_date else None
        return instance

