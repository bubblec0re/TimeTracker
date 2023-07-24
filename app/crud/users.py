from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User_ORM
from app.utils import hash_password
from fastapi import HTTPException, status


def create_user(new_user: UserCreate, db: Session) -> User_ORM:
    q = db.query(User_ORM).filter(User_ORM.name == new_user.name)
    if db.query(q.exists()).scalar():
        raise HTTPException(status.HTTP_409_CONFLICT, "A user with that name already exists")
    q = db.query(User_ORM).filter(User_ORM.email == new_user.email)
    if db.query(q.exists()).scalar():
        raise HTTPException(status.HTTP_409_CONFLICT, "A user with that e-mail address already exists")

    new_db_user = User_ORM(
        name=new_user.name,
        email=new_user.email,
        password=hash_password(new_user.password),
    )

    db.commit()
    return new_db_user
