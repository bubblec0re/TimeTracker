# PYDANTIC MODELS

# Work types: study, relax, job, walking outside, etc.
# work records: work type + description + start datetime and end datetime ('job, fixing errors, 2023.04.13 11:00, 2023.04.13 19:45')
# users: name, email

from pydantic import BaseModel, Field
from datetime import datetime
from .worktypes import Worktype


class WorkrecordBase(BaseModel):
    name: str
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)


class Workrecord_create(WorkrecordBase):
    type_id: int


class Workrecord_update(WorkrecordBase):
    type_id: int


class Workrecord(WorkrecordBase):
    id: int
    type: Worktype

    class Config:
        orm_mode = True
