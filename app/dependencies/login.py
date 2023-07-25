from datetime import datetime
from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError

from app.settings import algorithm, jwt_secret_key

reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/users/login", scheme_name="JWT")

async def get_token_data(token: str = Depends(reuseable_oauth)) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])

        if datetime.fromtimestamp(payload['exp']) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return payload
