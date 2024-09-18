from fastapi import APIRouter

from app.core.dependencies import CurrentUser
from app.core.enums import UserRoles
from app.core.security import authorize

router = APIRouter(prefix="/converter", tags=["Converter"])


@router.post("/upload")
@authorize(role=[UserRoles.MODERATOR, UserRoles.BASE_USER])
async def upload(current_user: CurrentUser):
    from icecream import ic

    ic(current_user)


@router.get("/download")
async def download():
    pass
