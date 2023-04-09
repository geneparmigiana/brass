from typing import Optional

from pydantic import BaseModel


class AuthToken(BaseModel):
    access_token: str
    token_type: str


class AuthTokenPayload(BaseModel):
    sub: Optional[int] = None
