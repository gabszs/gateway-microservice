import aiobotocore.session

from app.core.settings import settings


class AsyncS3Manager:
    def __init__(
        self,
        s3_access_key_id: str = settings.s3_access_key,
        s3_secret_access_key: str = settings.s3_secret_key,
        region_name: str = "auto",
        endpoint_url: str = settings.s3_endpoint,
    ):
        self.s3_access_key_id = s3_access_key_id
        self.s3_secret_access_key = s3_secret_access_key
        self.region_name = region_name
        self.endpoint_url = endpoint_url
        self.session = aiobotocore.session.get_session()

    async def _create_client(self):
        return self.session.create_client(
            service_name="s3",
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.s3_access_key_id,
            aws_secret_access_key=self.s3_secret_access_key,
            region_name=self.region_name,
        )

    async def bucket_exists(self, bucket_name: str) -> bool:
        async with await self._create_client() as client:
            response = await client.list_buckets()
            buckets = [bucket["Name"] for bucket in response["Buckets"]]
            return bucket_name in buckets

    async def put_object(self, bucket_name: str, key: str, data: bytes) -> dict:
        async with await self._create_client() as client:
            resp = await client.put_object(Bucket=bucket_name, Key=key, Body=data)
            return resp

    async def get_object(self, bucket_name: str, key: str) -> dict:
        async with await self._create_client() as client:
            response = await client.get_object(Bucket=bucket_name, Key=key)
            async with response["Body"] as stream:
                data = await stream.read()
            return {
                "Content": data,
                "ContentType": response.get("ContentType", "application/octet-stream"),
            }

    async def delete_object(self, bucket_name: str, key: str) -> dict:
        async with await self._create_client() as client:
            resp = await client.delete_object(Bucket=bucket_name, Key=key)
            return resp

    async def list_objects(self, bucket_name: str, prefix: str) -> list:
        async with await self._create_client() as client:
            paginator = client.get_paginator("list_objects")
            objects = []
            async for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
                for obj in page.get("Contents", []):
                    objects.append(obj)
            return objects
