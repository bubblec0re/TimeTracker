from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.crud as crud
from app.dependencies import get_session
from app.models import Worktype_ORM
from app.schemas import Worktype, Worktype_create, Worktype_update

######### WORKTYPES
worktypes_router = APIRouter(prefix="/worktypes")


@worktypes_router.get("/", response_model=list[Worktype])
async def worktypes(db: Session = Depends(get_session)) -> list[Worktype_ORM]:
    return crud.worktypes(db)


@worktypes_router.get("/{id}", response_model=Worktype)
async def worktype(id: int, db: Session = Depends(get_session)) -> Worktype:
    return crud.worktype(id, db)


@worktypes_router.post("/new", response_model=Worktype)
async def add_worktype(
    worktype: Worktype_create, db: Session = Depends(get_session)
) -> Worktype:
    return crud.create_worktype(worktype, db)


@worktypes_router.post("/update/{id}")
async def update_worktype(
    id: int, new_worktype: Worktype_update, db: Session = Depends(get_session)
) -> Worktype:
    return crud.update_worktype(id, new_worktype, db)


@worktypes_router.delete("/delete/{id}")
async def delete_worktype(id: int, db: Session = Depends(get_session)):
    return crud.delete_worktype(id, db)
