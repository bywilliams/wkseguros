from sqlalchemy.orm import Session

from wkseguros.backend.models.user import User
from wkseguros.backend.schemas.user import UserCreate
from wkseguros.backend.services.auth import hash_password


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()