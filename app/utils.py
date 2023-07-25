from datetime import datetime, timedelta

from jose import jwt
from passlib.hash import bcrypt

from app.settings import (access_token_expire_minutes, algorithm,
                          jwt_secret_key, jwt_secret_refresh_key,
                          refresh_token_expire_minutes)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return bcrypt.hash(password)


def create_access_token(name: str, id: int) -> str:
    return create_token(name, id, jwt_secret_key, access_token_expire_minutes)


def create_refresh_token(name: str, id: int) -> str:
    return create_token(name, id, jwt_secret_refresh_key, refresh_token_expire_minutes)


def create_token(name: str, id: int, key: str, delta: int) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=delta)
    to_encode = {"exp": expires_delta, "sub": name, "id": id}
    encoded_jwt = jwt.encode(to_encode, key, algorithm)
    return encoded_jwt
