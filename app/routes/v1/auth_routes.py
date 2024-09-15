from fastapi import APIRouter

from app.core.dependencies import AuthServiceDependency
from app.schemas.auth_schema import SignIn

router = APIRouter(prefix="/auth", tags=["Auth"])


# @router.post("/sign-in", response_model=SignInResponse)
@router.post("/sign-in")
async def sign_in(user_info: SignIn, service: AuthServiceDependency):
    return await service.sign_in(user_info)
