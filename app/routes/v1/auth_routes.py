from fastapi import APIRouter

from app.core.dependencies import AuthServiceDependency
from app.schemas.auth_schema import SignIn
from app.schemas.auth_schema import SignInResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign-in", response_model=SignInResponse)
async def sign_in(user_info: SignIn, service: AuthServiceDependency):
    return await service.sign_in(user_info)
