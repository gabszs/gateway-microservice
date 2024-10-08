from typing import Annotated

from aiohttp import ClientSession
from fastapi import Depends
from pika.adapters.blocking_connection import BlockingChannel

from app.core.exceptions import AuthError
from app.core.http_client import get_async_client
from app.core.security import JWTBearer
from app.core.settings import settings
from app.helpers import AsyncS3Manager
from app.helpers.rabbit_manager import get_rabbit_channel
from app.schemas.user_schema import User
from app.schemas.user_schema import User as UserSchema
from app.services import AuthService
from app.services import ConverterService

async_s3 = AsyncS3Manager()


async def get_current_user(user_credentials: UserSchema = Depends(JWTBearer())) -> UserSchema:
    return user_credentials


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise AuthError("Inactive user")
    return current_user


async def get_auth_service(client: ClientSession = Depends(get_async_client)) -> AuthService:
    return AuthService(client=client)


async def get_save_service(channel: BlockingChannel = Depends(get_rabbit_channel)) -> ConverterService:
    return ConverterService(async_s3, bucket_name=settings.upload_bucket_name, rabbit_channel=channel)


AuthServiceDependency = Annotated[AuthService, Depends(get_auth_service)]
CurrentUser = Annotated[User, Depends(get_current_user)]
CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]
SaveBucket = Annotated[ConverterService, Depends(get_save_service)]
