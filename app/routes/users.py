from fastapi import APIRouter, Depends
from app.dependencies import get_session
from app.schemas import UserCreate
import app.crud as crud

users_router = APIRouter(prefix='/users')


@users_router.post("/register")
async def register_user(new_user: UserCreate,db = Depends(get_session)):
    crud.create_user(new_user, db)