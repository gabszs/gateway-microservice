from aiohttp import ClientSession


class AuthService:
    def __init__(self, client: ClientSession):
        self.client = client

    def sign_in(self, schema):
        print(schema)
