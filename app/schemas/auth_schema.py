from pydantic import BaseModel
from pydantic import EmailStr


class SignIn(BaseModel):
    email__eq: EmailStr
    password: str


class SignInResponse(BaseModel):
    access_token: str
    expiration: str
