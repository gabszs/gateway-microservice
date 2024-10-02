import os

import pika
from fastapi import UploadFile
from fastapi.responses import StreamingResponse
from pika.adapters.blocking_connection import BlockingChannel
from pydantic import EmailStr

from app.core.exceptions import BadRequestError
from app.core.object_storage import AsyncS3Manager
from app.core.settings import settings
from app.schemas.file_schema import QueueMessage


class ConverterService:
    def __init__(self, async_s3: AsyncS3Manager, bucket_name: str, rabbit_channel: BlockingChannel) -> None:
        self.async_s3 = async_s3
        self.bucket_name = bucket_name
        self.rabbit_channel = rabbit_channel

    async def upload_video_file(self, file: UploadFile, client_email: EmailStr) -> None:
        queue_message = QueueMessage(
            file_name=file.filename, content_type=file.content_type, client_email=client_email, download_link=None
        )
        data = await file.read()
        key = os.path.basename(queue_message.file_name)

        try:
            await self.async_s3.put_object(
                bucket_name=self.bucket_name,
                key=key,  # type: ignore
                data=bytes(data),
            )
        except Exception as error:
            raise error
        await self.publish_message(queue_message.file_name, queue_message)
        # se for retornar, vai ser por que preciso retornar o id desse arqruivo
        # mas como o id e o proprio nome do arquivo, entao podemos usar ele e nao
        # precisamos retornar o id, ----- VOU CHECKAR COM SENIOR PARA VER QUAL A ACAO MAIS LOGICA

    async def download_video_file(self, object_name: str):
        response = await self.async_s3.get_object(self.bucket_name, key=object_name)
        content = response["Content"]
        content_type = response.get("ContentType", "application/octet-stream")

        return StreamingResponse(bytes(content), media_type=content_type)

    async def remove_video_file(self, object_name: str):
        await self.async_s3.delete_object(self.bucket_name, object_name)

    async def publish_message(self, object_name: str, queue_message: QueueMessage):
        try:
            self.rabbit_channel.basic_publish(
                exchange=settings.UPLOAD_EXCHANGE,
                routing_key=settings.UPLOAD_ROUTING_KEY,
                body=queue_message.model_dump_json(),
                properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
            )
        except Exception as _:
            await self.remove_video_file(object_name)
            raise BadRequestError(detail="Error while trying to convert the file")
