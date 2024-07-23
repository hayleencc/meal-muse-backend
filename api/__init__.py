from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from adapters.src.repositories.sql.config import SessionManager, SQLConnection
from api.src.routers import recipe_router, router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    connection: SQLConnection = SQLConnection()
    SessionManager.initialize_session(connection)
    yield
    SessionManager.close_session()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    app.include_router(recipe_router)
    return app
