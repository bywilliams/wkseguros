from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from wkseguros.backend.core.services.auth import AuthService
from wkseguros.backend.utils.dependencies import get_db
from wkseguros.backend.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post('/login', response_model=UserResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        authenticated_user = auth_service.authenticate_user(user.email, user.password)
        return authenticated_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@router.post('/add_user', response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        new_user = auth_service.add_user(user.username, user.email, user.password, user.access_level_id)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
