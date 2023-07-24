# PYDANTIC MODELS
# Work types: study, relax, job, walking outside, etc.


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
