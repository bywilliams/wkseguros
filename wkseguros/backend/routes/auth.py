from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from wkseguros.backend.dependencies import get_db
from wkseguros.backend.models.user import User
from wkseguros.backend.repositories.user_repository import create_user
from wkseguros.backend.schemas.user import UserCreate, UserResponse

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('/login', response_model=UserResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
        )
    return db_user


@router.post('/users/', response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
