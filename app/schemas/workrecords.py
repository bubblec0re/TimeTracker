# PYDANTIC MODELS
# work records: owner + work type + description + start datetime and end datetime
#i. e. 'work, fixing errors, 2023.04.13 11:00, 2023.04.13 19:45'


from datetime import datetime

from pydantic import BaseModel, Field

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
