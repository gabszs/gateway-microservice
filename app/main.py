from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.v1 import routers


def init_app():
    lifespan = None

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        yield

    app = FastAPI(
        title="CV-Api",
        description="Gateway Application built for manamengt of diverse service dedicated to audio/video conversion",
        contact={
            "name": "Gabriel Carvalho",
            "url": "https://www.linkedin.com/in/gabzsz/",
            "email": "gabriel.carvalho@huawei.com",
        },
        summary="WebAPI built on best market practices such as TDD, Clean Architecture, Data Validation with Pydantic V2",
        lifespan=lifespan,
    )
    app.include_router(routers)

    return app


app = init_app()
