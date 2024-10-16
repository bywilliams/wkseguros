from passlib.context import CryptContext
from sqlalchemy.orm import Session

from wkseguros.backend.repositories.user_repository import UserRepository

# Contexto de criptografia
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and self.verify_password(password, user.password):
            return user
        raise ValueError('Invalid credentials')

    def add_user(
        self, username: str, email: str, password: str, access_level_id: int
    ):
        hashed_pw = self.hash_password(password)
        return self.user_repository.create_user(
            username, email, hashed_pw, access_level_id
        )

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
