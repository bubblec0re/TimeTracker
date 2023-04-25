# PYDANTIC MODELS

# Work types: study, relax, job, walking outside, etc.
# work records: work type + description + start datetime and end datetime ('job, fixing errors, 2023.04.13 11:00, 2023.04.13 19:45')
# users: name, email

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str = "Default user"
    email: str


class UserCreate(UserBase):
    password_hash: str


class User(UserBase):
    name: str = "Default user"
    email: str
