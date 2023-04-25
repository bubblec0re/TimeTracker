import app.crud as crud
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import Workrecord, Workrecord_create, Workrecord_update
from app.db import get_session

########## WORKRECORDS
workrecords_router = APIRouter()


@workrecords_router.get("/workrecords", response_model=list[Workrecord])
async def workrecords(db: Session = Depends(get_session)):
    return crud.workrecords(db)


@workrecords_router.get("/workrecords/{id}", response_model=Workrecord)
async def workrecord(id: int, db: Session = Depends(get_session)):
    return crud.workrecord(id, db)


@workrecords_router.post("/workrecords/new", response_model=Workrecord)
async def add_workrecord(
    new_workrecord: Workrecord_create, db: Session = Depends(get_session)
) -> Workrecord:
    return crud.create_workrecord(new_workrecord, db)


@workrecords_router.post("/workrecords/update/{id}", response_model=Workrecord)
async def update_workrecord(
    id: int, new_workrecord: Workrecord_update, db: Session = Depends(get_session)
) -> Workrecord:
    return crud.update_workrecord(id, new_workrecord, db)


@workrecords_router.delete("/workrecords/delete/{id}")
async def delete_workrecord(id: int, db: Session = Depends(get_session)):
    return crud.delete_workrecord(id, db)
