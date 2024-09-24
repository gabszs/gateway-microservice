from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectionError

from app.core.exceptions import AuthError
from app.core.exceptions import BadRequestError
from app.core.settings import settings
from app.schemas.auth_schema import SignIn


class AuthService:
    def __init__(self, client: ClientSession):
        self.client = client

    async def sign_in(self, schema: SignIn):
        url = settings.auth_service_url
        try:
            async with self.client.post(f"{url}/sign-in", json=schema.model_dump()) as response:
                data = await response.json()
                if response.status != 200:
                    raise AuthError(detail=data["detail"])
                return data
        except ClientConnectionError as _:
            raise BadRequestError(detail="Auth Service not available")
