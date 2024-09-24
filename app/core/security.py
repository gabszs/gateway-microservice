from functools import wraps
from typing import List

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectionError
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from app.core.exceptions import AuthError
from app.core.exceptions import BadRequestError
from app.core.http_client import get_async_client
from app.core.settings import Settings
from app.schemas.user_schema import User as UserSchema

settings = Settings()


def authorize(role: List[str], allow_same_id: bool = False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user_role = kwargs.get("current_user").role
            have_authorization = user_role in role
            if allow_same_id:
                is_same_id = kwargs.get("current_user").id == kwargs.get("user_id")
                if not is_same_id and not have_authorization:
                    raise AuthError("Not enough permissions")
                return await func(*args, **kwargs)
            if not have_authorization:
                raise AuthError("Not enough permissions")
            return await func(*args, **kwargs)

        return wrapper

    return decorator


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> UserSchema | None:  # type: ignore
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if not credentials:
            raise AuthError(detail="Invalid authorization code")

        if credentials.scheme != "Bearer":
            raise AuthError(detail="Invalid authentication scheme")

        async for client in get_async_client():
            status_code, data = await self.get_data_from_token(credentials.credentials, client)
            if status_code != 200:
                raise AuthError(detail=data["detail"])
            return data

    async def get_data_from_token(self, token: str, client: ClientSession) -> tuple[int, UserSchema]:
        token = f"Bearer {token}"

        try:
            async with client.get(f"{settings.auth_service_url}/me", headers={"Authorization": token}) as response:
                status_code = response.status
                data = await response.json()
                if status_code != 200:
                    raise AuthError(detail=data["detail"])

                return status_code, UserSchema(**data)
        except ClientConnectionError as _:
            raise BadRequestError(detail="Auth Service not available")
