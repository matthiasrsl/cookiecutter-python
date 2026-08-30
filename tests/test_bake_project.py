"""Bakes representative option combinations and runs each generated
project's own tooling (uv sync, ruff, mypy, pytest) against the result.
"""

import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

TEMPLATE_DIR = Path(__file__).resolve().parent.parent

BASE_CONTEXT = {
    "project_name": "Test Project",
    "author_name": "Test Author",
    "author_email": "test@example.com",
}

COMBOS = {
    "data_science": {"project_type": "data_science"},
    "fastapi-no-docker": {"project_type": "fastapi", "use_docker": "no"},
    "fastapi-docker": {"project_type": "fastapi", "use_docker": "yes"},
    "django-plain": {"project_type": "django", "django_flavor": "plain"},
    "django-drf": {"project_type": "django", "django_flavor": "drf"},
    "django-ninja": {"project_type": "django", "django_flavor": "ninja"},
    "django-docker": {"project_type": "django", "django_flavor": "plain", "use_docker": "yes"},
    "all-tools-off": {
        "project_type": "fastapi",
        "use_ruff": "no",
        "use_mypy": "no",
        "use_bandit": "no",
        "use_pyscn": "no",
        "use_conventional_commits": "no",
    },
    "all-tools-on": {
        "project_type": "fastapi",
        "use_ruff": "yes",
        "use_mypy": "yes",
        "use_bandit": "yes",
        "use_pyscn": "yes",
        "use_conventional_commits": "yes",
    },
}


def bake(tmp_path: Path, **extra_context: str) -> Path:
    context = {**BASE_CONTEXT, **extra_context}
    cookiecutter(
        str(TEMPLATE_DIR),
        no_input=True,
        extra_context=context,
        output_dir=str(tmp_path),
    )
    project_dirs = list(tmp_path.iterdir())
    assert len(project_dirs) == 1
    return project_dirs[0]


def run(cmd: list[str], cwd: Path) -> None:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    assert result.returncode == 0, (
        f"{' '.join(cmd)} failed in {cwd}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )


@pytest.mark.parametrize("context", COMBOS.values(), ids=COMBOS.keys())
def test_bake_and_verify(tmp_path: Path, context: dict[str, str]) -> None:
    project_dir = bake(tmp_path, **context)

    run(["uv", "sync"], cwd=project_dir)

    if context.get("use_ruff", "yes") == "yes":
        run(["uv", "run", "ruff", "check", "."], cwd=project_dir)
        run(["uv", "run", "ruff", "format", "--check", "."], cwd=project_dir)

    if context.get("use_mypy", "yes") == "yes":
        run(["uv", "run", "mypy", "."], cwd=project_dir)

    run(["uv", "run", "pytest"], cwd=project_dir)


def test_pruned_files_absent(tmp_path: Path) -> None:
    project_dir = bake(tmp_path, project_type="fastapi", use_docker="no")

    assert not (project_dir / "manage.py").exists()
    assert not (project_dir / "data").exists()
    assert not (project_dir / "docker-compose.yml").exists()
    assert (project_dir / "src" / "test_project" / "main.py").exists()


def test_all_tools_off_omits_tool_references(tmp_path: Path) -> None:
    project_dir = bake(
        tmp_path,
        project_type="fastapi",
        use_ruff="no",
        use_mypy="no",
        use_bandit="no",
        use_pyscn="no",
        use_conventional_commits="no",
    )

    assert not (project_dir / ".pyscn.toml").exists()

    pyproject = (project_dir / "pyproject.toml").read_text()
    assert "[tool.ruff]" not in pyproject
    assert "[tool.mypy]" not in pyproject
    assert "[tool.bandit]" not in pyproject

    pre_commit_config = (project_dir / ".pre-commit-config.yaml").read_text()
    assert "ruff" not in pre_commit_config
    assert "mypy" not in pre_commit_config
    assert "bandit" not in pre_commit_config
    assert "pyscn" not in pre_commit_config
