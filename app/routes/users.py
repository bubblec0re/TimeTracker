from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

import app.crud as crud
from app.dependencies import get_session, get_token_data
from app.schemas import UserBase, UserCreate, UserLogin
from app.utils import create_access_token, create_refresh_token

users_router = APIRouter(prefix="/users")


@users_router.post("/register")
async def register_user(new_user: UserCreate, db=Depends(get_session)):
    crud.create_user(new_user, db)
    return new_user


@users_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_session)):
    creds = UserLogin(name=form_data.username, password=form_data.password)
    user = crud.find_user(creds, db)
    
    return {
        'access_token': create_access_token(user),
        'refresh_token': create_refresh_token(user)
    }


@users_router.get('/me', summary='Get details of currently logged in user', response_model=UserBase)
async def get_me(token: dict[str, Any] = Depends(get_token_data), db = Depends(get_session)):
    username:str = token['sub']
    user = crud.get_current_user(username, db)
    return UserBase(name=user.name, email=user.email) # type: ignore
