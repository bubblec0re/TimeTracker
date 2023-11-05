from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.crud as crud
from app.dependencies import get_session, get_id_from_token
from app.schemas import Workrecord, Workrecord_create, Workrecord_update

########## WORKRECORDS
workrecords_router = APIRouter(prefix="/workrecords")


@workrecords_router.get("/", response_model=list[Workrecord])
async def workrecords(db: Session = Depends(get_session)):
    return crud.workrecords(db)


@workrecords_router.get("/{id}", response_model=Workrecord)
async def workrecord(id: int, db: Session = Depends(get_session)):
    return crud.workrecord(id, db)


@workrecords_router.post("/new", response_model=Workrecord)
async def add_workrecord(new_workrecord: Workrecord_create, db: Session = Depends(get_session), author_id: int = Depends(get_id_from_token)) -> Workrecord:
    wr = crud.create_workrecord(new_workrecord, db)
    return wr


@workrecords_router.post("/update/{id}", response_model=Workrecord)
async def update_workrecord(
    id: int, new_workrecord: Workrecord_update, db: Session = Depends(get_session)
) -> Workrecord:
    return crud.update_workrecord(id, new_workrecord, db)


@workrecords_router.delete("/delete/{id}")
async def delete_workrecord(id: int, db: Session = Depends(get_session)):
    return crud.delete_workrecord(id, db)
