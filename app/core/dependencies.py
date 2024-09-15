from typing import Annotated

from aiohttp import ClientSession
from fastapi import Depends

from app.core.exceptions import AuthError
from app.core.security import JWTBearer
from app.schemas.user_schema import User
from app.schemas.user_schema import User as UserSchema
from app.services import AuthService


async def get_async_client() -> ClientSession:
    async with ClientSession() as session:
        yield session


async def get_jwt_bearer(client=Depends(get_async_client)):
    return JWTBearer(client=client)


async def get_current_user(user_credentials: UserSchema = Depends(get_jwt_bearer)) -> UserSchema:
    return user_credentials


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise AuthError("Inactive user")
    return current_user


async def get_auth_service(client: ClientSession = Depends(get_async_client)):
    return AuthService(client=client)


AuthServiceDependency = Annotated[AuthService, Depends(get_auth_service)]


CurrentUser = Annotated[User, Depends(get_current_user)]
CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]
