from aiohttp import ClientSession

from app.core.settings import settings
from app.schemas.auth_schema import SignIn


class AuthService:
    def __init__(self, client: ClientSession):
        self.client = client

    async def sign_in(self, schema: SignIn):
        url = settings.auth_service_url
        print("url: ", f"{url}/sign-in")
        async with self.client.post(f"{url}/sign-in", json=schema.model_dump()) as response:
            data = await response.json()
            return data
