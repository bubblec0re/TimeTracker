# PYDANTIC MODELS
# users: name, email, password


from pydantic import BaseModel


class UserBase(BaseModel):
    name: str = "Default user"


class UserCreate(UserBase):
    email: str
    password: str


class UserLogin(UserBase):
    name: str
    password: str


class UserInfo(UserBase):
    email: str
