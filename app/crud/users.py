from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User_ORM
from app.utils import hash_password, verify_password


def create_user(username: str, email: str, password: str, db: Session) -> User_ORM:
    q = db.query(User_ORM.id).filter(User_ORM.name == username)
    if db.query(q.exists()).scalar():
        raise HTTPException(
            status.HTTP_409_CONFLICT, "A user with that name or email already exists"
        )

    q = db.query(User_ORM.id).filter(User_ORM.email == email)
    if db.query(q.exists()).scalar():
        raise HTTPException(
            status.HTTP_409_CONFLICT, "A user with that name or email already exists"
        )

    new_db_user = User_ORM(
        name=username,
        email=email,
        password=hash_password(password),
    )

    db.add(new_db_user)
    db.commit()
    return new_db_user


def login_user(username: str, password: str, db: Session) -> User_ORM:
    q = db.query(User_ORM).filter(User_ORM.name == username)
    user = q.first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect login or password")

    if not verify_password(password, user.password):  # type: ignore
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect login or password")

    return user


def find_user_by_name(username: str, db: Session) -> dict[str, str]:
    q = db.query(User_ORM).filter(User_ORM.name == username)
    user = q.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return {"name": str(user.name), "email": str(user.email)}
