from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core.dependencies import rabbit_connection
from app.routes.v1 import routers


def init_app():
    lifespan = None

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        yield

        if rabbit_connection and rabbit_connection.is_open:
            rabbit_connection.close()

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5555)
