from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from app.settings import jwt_secret_key, jwt_secret_refresh_key

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"


def create_access_token(subject: str | Any) -> str:
    return create_token(subject, jwt_secret_key, ACCESS_TOKEN_EXPIRE_MINUTES)


def create_refresh_token(subject: str | Any) -> str:
    return create_token(subject, jwt_secret_refresh_key, REFRESH_TOKEN_EXPIRE_MINUTES)


def create_token(subject: str | Any, key: str, delta: int = 30) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=delta)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, key, ALGORITHM)
    return encoded_jwt
