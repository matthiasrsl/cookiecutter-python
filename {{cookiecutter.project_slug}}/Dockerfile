FROM python:{{ cookiecutter.python_version }}-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --no-install-project

COPY . .
RUN uv sync

{% if cookiecutter.project_type == "fastapi" %}
CMD ["uv", "run", "uvicorn", "{{ cookiecutter.package_name }}.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
{% elif cookiecutter.project_type == "django" %}
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
{% endif %}
