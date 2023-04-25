from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from app.schemas import Worktype_create, Worktype_update
from app.models import Worktype_ORM


def worktypes(db: Session) -> list[Worktype_ORM]:
    db_wt = db.query(Worktype_ORM).all()
    if not db_wt:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return db_wt


def worktype(id: int, db: Session) -> Worktype_ORM:
    worktype = db.query(Worktype_ORM).filter(Worktype_ORM.id == id).first()
    return worktype


def create_worktype(worktype: Worktype_create, db: Session) -> Worktype_ORM:
    new_wt = Worktype_ORM(name=worktype.name)
    db.add(new_wt)
    db.commit()
    return new_wt


def update_worktype(
    id: int, new_worktype: Worktype_update, db: Session
) -> Worktype_ORM:
    db_wt = worktype(id, db)
    for key, value in new_worktype.dict().items():
        setattr(db_wt, key, value) if value else None
    db.commit()
    db.refresh(db_wt)
    return db_wt


def delete_worktype(id: int, db: Session):
    db_wt = worktype(id, db)
    db.delete(db_wt)
    db.commit()
    return Response()
