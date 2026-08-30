# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Getting started

This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies.

```bash
uv sync
```

{% if cookiecutter.project_type == "data_science" %}
Register the project's virtualenv as a Jupyter kernel (useful for VS Code notebooks):

```bash
uv run python -m ipykernel install --user --name {{ cookiecutter.package_name }}
```

{% elif cookiecutter.project_type == "fastapi" %}
Run the API locally:

```bash
uv run uvicorn {{ cookiecutter.package_name }}.main:app --reload
```

{% if cookiecutter.use_docker == "yes" %}
Or with Docker (includes a Postgres database with hot reload):

```bash
docker compose up
```

{% endif %}
{% elif cookiecutter.project_type == "django" %}
Run the development server:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

{% if cookiecutter.use_docker == "yes" %}
Or with Docker (includes a Postgres database with hot reload):

```bash
docker compose up
```

{% endif %}
{% endif %}
## Quality tooling

```bash
uv run pytest
{% if cookiecutter.use_ruff == "yes" %}
uv run ruff check .
uv run ruff format .
{% endif %}
{% if cookiecutter.use_mypy == "yes" %}
uv run mypy .
{% endif %}
{% if cookiecutter.use_bandit == "yes" %}
uv run bandit -r src
{% endif %}
{% if cookiecutter.use_pyscn == "yes" %}
uv run pyscn check src
{% endif %}
```
{% if cookiecutter.use_conventional_commits == "yes" %}

## Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/). Install the git hooks with:

```bash
uv run pre-commit install --hook-type pre-commit --hook-type commit-msg
```
{% endif %}
