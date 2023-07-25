from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from app.models import Workrecord_ORM
from app.schemas import Workrecord_create, Workrecord_update


def workrecords(db: Session) -> list[Workrecord_ORM]:
    return db.query(Workrecord_ORM).all()


def workrecord(id: int, db: Session) -> Workrecord_ORM:
    db_wr = db.query(Workrecord_ORM).filter(Workrecord_ORM.id == id).first()
    if not db_wr:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return db_wr


def create_workrecord(new_workrecord: Workrecord_create, db: Session) -> Workrecord_ORM:
    db_workrecord = Workrecord_ORM(**new_workrecord.dict())
    db.add(db_workrecord)
    db.commit()
    return db_workrecord


def update_workrecord(id: int, new_workrecord: Workrecord_update, db: Session):
    db_wr = workrecord(id, db)
    for key, value in new_workrecord.dict().items():
        setattr(db_wr, key, value) if value else None
    db.commit()
    db.refresh(db_wr)
    return db_wr


def delete_workrecord(id: int, db: Session):
    db_wr = workrecord(id, db)
    db.delete(db_wr)
    db.commit()
    return Response()
