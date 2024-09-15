from pydantic import BaseModel


class SignIn(BaseModel):
    email__eq: str
    password: str
