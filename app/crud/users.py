from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_session
from app.models import User_ORM
from app.schemas import UserCreate, UserLogin
from app.utils import hash_password, verify_password


def create_user(new_user: UserCreate, db: Session) -> User_ORM:
    q = db.query(User_ORM.id).filter(User_ORM.name == new_user.name)
    if db.query(q.exists()).scalar():
        raise HTTPException(
            status.HTTP_409_CONFLICT, "A user with that name or email already exists"
        )

    q = db.query(User_ORM.id).filter(User_ORM.email == new_user.email)
    if db.query(q.exists()).scalar():
        raise HTTPException(
            status.HTTP_409_CONFLICT, "A user with that name or email already exists"
        )

    new_db_user = User_ORM(
        name=new_user.name,
        email=new_user.email,
        password=hash_password(new_user.password),
    )

    db.add(new_db_user)
    db.commit()
    return new_db_user


def find_user(creds: UserLogin, db: Session) -> User_ORM:
    q = db.query(User_ORM).filter(User_ORM.name == creds.name)
    user = q.first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect login or password")

    if not verify_password(creds.password, user.password):  # type: ignore
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect login or password")

    return user


def get_current_user(username: str, db: Session) -> User_ORM:

    q = db.query(User_ORM).filter(User_ORM.name == username)
    user = q.first()
    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

    return user
