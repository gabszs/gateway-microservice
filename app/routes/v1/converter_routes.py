from typing import Annotated

from fastapi import APIRouter
from fastapi import File
from fastapi import status
from fastapi import UploadFile
from pydantic import EmailStr

from app.core.dependencies import CurrentUser
from app.core.dependencies import SaveBucket
from app.core.enums import UserRoles
from app.core.security import authorize

router = APIRouter(prefix="/converter", tags=["Converter"])
fileUpload = Annotated[UploadFile, File(description="A file read as UploadFile")]


@router.post("/upload/{email}", status_code=status.HTTP_204_NO_CONTENT)
@authorize(role=[UserRoles.MODERATOR, UserRoles.BASE_USER])
async def upload(email: EmailStr, file: fileUpload, service: SaveBucket, current_user: CurrentUser):
    await service.upload_video_file(file, client_email=email)
