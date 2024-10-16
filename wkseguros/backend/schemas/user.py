from pydantic import BaseModel, EmailStr


# Base para user
class UserBase(BaseModel):
    email: EmailStr


# Modelo para criação
class UserCreate(UserBase):
    password: str


# Modelo para exibição
class UserResponse(UserBase):
    id: int
    username: str
    access_level_id: int

    class Config:
        orm_mode = True
