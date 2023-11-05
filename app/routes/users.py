from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

import app.crud as crud
from app.dependencies import get_session, get_token_payload, get_id_from_token
from app.schemas import UserCreate, UserInfo
from app.utils import create_access_token, create_refresh_token

users_router = APIRouter(prefix="/users")


@users_router.post("/register", response_model=UserCreate)
async def register_user(new_user: UserCreate, db=Depends(get_session)):
    crud.create_user(new_user.name, new_user.email, new_user.password, db)
    return new_user


@users_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db=Depends(get_session)):
    user = crud.login_user(form_data.username, form_data.password, db)

    return {
        "access_token": create_access_token(user.name, user.id),  # type: ignore
        "refresh_token": create_refresh_token(user.name, user.id),  # type: ignore
    }


@users_router.get("/me", response_model=UserInfo)
async def get_me(token: dict[str, Any] = Depends(get_token_payload),
                 db=Depends(get_session)) -> UserInfo:
    user = crud.find_user_by_name(token["sub"], db)
    return UserInfo(**user)

@users_router.get("/me_id")
async def get_me_id(id: int = Depends(get_id_from_token)) -> int:
    return id
