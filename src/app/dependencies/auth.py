from typing import List

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError

from app.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    roles: List[str]


async def decode_jwt(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        decoded_token = jwt.decode(
            token, settings.AUTH.SECRET_KEY, algorithms=[settings.AUTH.ALGORITHM]
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        return TokenData(**decoded_token)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )


async def check_for_subscription(token_data: TokenData = Depends(decode_jwt)) -> bool:
    return "subscriber" in token_data.roles
