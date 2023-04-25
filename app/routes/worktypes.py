import app.crud as crud
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Worktype_ORM
from app.schemas import Worktype, Worktype_create, Worktype_update
from app.db import get_session


######### WORKTYPES
worktypes_router = APIRouter()


@worktypes_router.get("/worktypes", response_model=list[Worktype])
async def worktypes(db: Session = Depends(get_session)) -> list[Worktype_ORM]:
    return crud.worktypes(db)


@worktypes_router.get("/worktypes/{id}", response_model=Worktype)
async def worktype(id: int, db: Session = Depends(get_session)) -> Worktype:
    return crud.worktype(id, db)


@worktypes_router.post("/worktypes/new", response_model=Worktype)
async def add_worktype(
    worktype: Worktype_create, db: Session = Depends(get_session)
) -> Worktype:
    return crud.create_worktype(worktype, db)


@worktypes_router.post("/worktypes/update/{id}")
async def update_worktype(
    id: int, new_worktype: Worktype_update, db: Session = Depends(get_session)
) -> Worktype:
    return crud.update_worktype(id, new_worktype, db)


@worktypes_router.delete("/worktypes/delete/{id}")
async def delete_worktype(id: int, db: Session = Depends(get_session)):
    return crud.delete_worktype(id, db)
