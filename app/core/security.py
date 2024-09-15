from functools import wraps
from typing import List

from aiohttp import ClientSession
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from app.core.exceptions import AuthError
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
    def __init__(self, client: ClientSession, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        self.client = client

    async def __call__(self, request: Request) -> UserSchema | None:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if not credentials:
            raise AuthError(detail="Invalid authorization code")

        if credentials.scheme != "Bearer":
            raise AuthError(detail="Invalid authentication scheme")

        status_code, data = await self.get_data_from_token(credentials.credentials)
        if status_code != 200:
            raise AuthError(detail="Invalid token or expired token")
        return data

    async def get_data_from_token(self, token: str) -> tuple[int, UserSchema]:
        async with self.client.get(settings.auth_service_url, headers={"Authorization": token}) as response:
            status_code = response.status
            data = await response.json()
            return status_code, UserSchema(**data)
