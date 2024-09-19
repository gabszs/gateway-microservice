from typing import Annotated

from aiohttp import ClientSession
from fastapi import Depends

from app.core.exceptions import AuthError
from app.core.http_client import get_async_client
from app.core.object_storage import AsyncMinioManager
from app.core.security import JWTBearer
from app.core.settings import settings
from app.schemas.user_schema import User
from app.schemas.user_schema import User as UserSchema
from app.services import AuthService
from app.services import MinioService

async_minio = AsyncMinioManager()


async def get_current_user(user_credentials: UserSchema = Depends(JWTBearer())) -> UserSchema:
    return user_credentials


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise AuthError("Inactive user")
    return current_user


async def get_auth_service(client: ClientSession = Depends(get_async_client)) -> AuthService:
    return AuthService(client=client)


async def get_save_service() -> MinioService:
    return MinioService(async_minio, bucket_name=settings.upload_bucket_name)


AuthServiceDependency = Annotated[AuthService, Depends(get_auth_service)]
CurrentUser = Annotated[User, Depends(get_current_user)]
CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]
SaveBucket = Annotated[MinioService, Depends(get_save_service)]
