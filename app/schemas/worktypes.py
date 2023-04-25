# PYDANTIC MODELS

# Work types: study, relax, job, walking outside, etc.
# work records: work type + description + start datetime and end datetime ('job, fixing errors, 2023.04.13 11:00, 2023.04.13 19:45')
# users: name, email

from pydantic import BaseModel


class WorktypeBase(BaseModel):
    name: str


class Worktype_create(WorktypeBase):
    pass


class Worktype_update(WorktypeBase):
    pass


class Worktype(WorktypeBase):
    id: int

    class Config:
        orm_mode = True
