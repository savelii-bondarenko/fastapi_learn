from fastapi import APIRouter
from pydantic import BaseModel
from Data.models import Users
from passlib.context import CryptContext
from Data.db import db_dependency

router = APIRouter(
    tags=["Auth controllers"]
)

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

@router.post("/auth")
async def create_user(user_request: CreateUserRequest, db: db_dependency):
    user_request = Users(
        username=user_request.username,
        email=user_request.email,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=PWD_CONTEXT.hash(user_request.password),
        role=user_request.role
    )
    

