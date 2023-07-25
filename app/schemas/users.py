# PYDANTIC MODELS
# users: name, email, password


from pydantic import BaseModel


class UserBase(BaseModel):
    name: str = "Default user"
    email: str|None


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    name: str
    password: str
