# PYDANTIC MODELS
# work records: owner + work type + description + start datetime and end datetime
#i. e. 'work, fixing errors, 2023.04.13 11:00, 2023.04.13 19:45'

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from .worktypes import Worktype
from .users import UserInfo


class WorkrecordBase(BaseModel):
    name: str
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)


class Workrecord_create(WorkrecordBase):
    author_id: int
    type_id: int


class Workrecord_update(WorkrecordBase):
    type_id: int


class Workrecord(WorkrecordBase):
    id: int
    type: Worktype
    author: Optional[UserInfo] # for now

    class Config:
        orm_mode = True
