from fastapi import FastAPI

from {{ cookiecutter.package_name }}.api.health import router as health_router
from {{ cookiecutter.package_name }}.core.config import settings
{% if cookiecutter.use_docker == "yes" %}
from {{ cookiecutter.package_name }}.core.db import lifespan

app = FastAPI(title=settings.app_name, lifespan=lifespan)
{% else %}

app = FastAPI(title=settings.app_name)
{% endif %}

app.include_router(health_router)
