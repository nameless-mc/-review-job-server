from fastapi import Cookie
from pydantic import BaseModel


class SigninCookie(BaseModel):
    token: str
    id: str
