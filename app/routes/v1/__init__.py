from fastapi import APIRouter

from app.routes.v1.auth_routes import router as auth_router
from app.routes.v1.converter_routes import router as converter_router
from app.routes.v1.ping_route import router as ping_router

routers = APIRouter(prefix="/v1")
router_list = [auth_router, converter_router, ping_router]

for router in router_list:
    routers.include_router(router)

__all__ = ["routers"]
