from sqlalchemy.orm import Session

from wkseguros.backend.models.access_level import AccessLevel
from wkseguros.backend.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self, username: str, email: str, password: str, access_level_id: int
    ) -> User:
        access_level = (
            self.db.query(AccessLevel)
            .filter(AccessLevel.id == access_level_id)
            .first()
        )
        if not access_level:
            raise ValueError(f'Nível de acesso {access_level_id} não encontrado.')

        new_user = User(
            username=username,
            email=email,
            password=password,
            access_level_id=access_level_id,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
