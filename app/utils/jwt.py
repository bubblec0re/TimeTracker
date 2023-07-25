from datetime import datetime, timedelta

from jose import jwt

from app.models import User_ORM
from app.settings import (access_token_expire_minutes, algorithm,
                          jwt_secret_key, jwt_secret_refresh_key,
                          refresh_token_expire_minutes)


def create_access_token(subject: User_ORM) -> str:
    return create_token(subject, jwt_secret_key, access_token_expire_minutes)


def create_refresh_token(subject: User_ORM) -> str:
    return create_token(subject, jwt_secret_refresh_key, refresh_token_expire_minutes)


def create_token(subject: User_ORM, key: str, delta: int = 30) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=delta)
    to_encode = {"exp": expires_delta, "sub": subject.name}
    encoded_jwt = jwt.encode(to_encode, key, algorithm)
    return encoded_jwt
