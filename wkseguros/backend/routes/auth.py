from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from wkseguros.backend.core.services.auth import AuthService
from wkseguros.backend.schemas.user import UserCreate, UserResponse
from wkseguros.backend.utils.dependencies import get_db

router = APIRouter()


@router.post('/add_user', response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        new_user = auth_service.add_user(
            user.username, user.email, user.password, user.access_level_id
        )
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
