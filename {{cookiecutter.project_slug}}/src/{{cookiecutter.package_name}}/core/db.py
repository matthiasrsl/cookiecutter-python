from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from {{ cookiecutter.package_name }}.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.db_pool = await asyncpg.create_pool(settings.database_url)
    try:
        yield
    finally:
        await app.state.db_pool.close()
