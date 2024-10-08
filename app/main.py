from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.helpers.rabbit_manager import rabbit_manager
from app.routes.v1 import routers

# http://localhost:5555/v1/converter/download?file_name=240925173542ee04_2024-07-08%2019-14-29.mp3


def init_app():
    lifespan = None

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        rabbit_manager.init()
        yield
        rabbit_manager.close_connection()

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
