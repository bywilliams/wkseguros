from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from wkseguros.config.database import SessionLocal
from wkseguros.backend.models.client import Client
from datetime import datetime

def add_client(name: str, last_name: str, cpf: str, born_date: datetime, address: str, email: str, phone: str):
    db: Session = SessionLocal()
    try:
        new_client = Client(
            name=name,
            last_name=last_name,
            cpf=cpf,
            born_date=born_date,
            address=address,
            email=email,
            phone=phone,
            created_at=datetime.now()
        )
        db.add(new_client)
        db.commit()
        print("Cliente adicionado com sucesso!")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao adicionar cliente: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    add_client("João", "Silva", "12345678901", datetime.strptime("1990-01-01", "%Y-%m-%d"), "Rua A, 123", "joao.silva@example.com", "11987654321")
