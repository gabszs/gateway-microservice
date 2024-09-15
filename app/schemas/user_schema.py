from typing import List

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr

from app.schemas.base_schema import ModelBaseInfo


class BaseUser(BaseModel):
    email: EmailStr
    username: str


class User(BaseUser, ModelBaseInfo):
    model_config = ConfigDict(from_attributes=True)

    is_active: bool
    role: List[str]
