# Python cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for scaffolding Python projects with a modern tooling baseline.

## Usage

```bash
uvx cookiecutter gh:<your-username>/python-cookiecutter
```

You'll be prompted for a project type (`data_science`, `fastapi`, or `django`) and a set of options controlling which quality tools (ruff, mypy, bandit, [pyscn](https://github.com/ludo-technologies/pyscn)), CI provider, Docker/Postgres setup, and license get included.

Every generated project uses [uv](https://docs.astral.sh/uv/) as its package manager.

## Developing this template

```bash
uv sync
uv run pytest
```

`tests/test_bake_project.py` bakes representative combinations of options and runs the generated project's own lint/type/test tooling against them.
