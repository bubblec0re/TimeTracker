from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User_ORM
from app.utils import hash_password

def create_user(new_user: UserCreate, db: Session):
    db_user = User_ORM(name=new_user.name, email=new_user.email, password = hash_password(new_user.password))
    db.add(db_user)
    db.commit()
    return db_user