from io import BytesIO

from fastapi import UploadFile
from fastapi.responses import StreamingResponse

from app.core.object_storage import AsyncMinioManager
from app.schemas.file_schema import FileMetadata


class MinioService:
    def __init__(self, minio: AsyncMinioManager, bucket_name: str) -> None:
        self.minio = minio
        self.bucket_name = bucket_name

    async def upload_video_file(self, file: UploadFile) -> None:
        file_metadata = FileMetadata(file_name=file.filename, content_type=file.content_type)
        data = await file.read()

        await self.minio.put_file(
            bucket_name=self.bucket_name,
            object_name=file_metadata.file_name,  # type: ignore
            data=BytesIO(data),
            length=len(data),
            content_type=file.content_type,
        )
        # se for retornar, vai ser por que preciso retornar o id desse arqruivo
        # mas como o id e o proprio nome do arquivo, entao podemos usar ele e nao
        # precisamos retornar o id, ----- VOU CHECKAR COM SENIOR PARA VER QUAL A ACAO MAIS LOGICA

    async def download_video_file(self, object_name: str):
        response = await self.minio.download_object(self.bucket_name, object_name=object_name)
        return StreamingResponse(
            response.content, media_type=response.headers.get("Content-Type", "application/octet-stream")
        )
