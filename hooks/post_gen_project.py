import os
import shutil

PROJECT_TYPE = "{{ cookiecutter.project_type }}"
DJANGO_FLAVOR = "{{ cookiecutter.django_flavor }}"
USE_DOCKER = "{{ cookiecutter.use_docker }}" == "yes"
CI_PROVIDER = "{{ cookiecutter.ci_provider }}"
LICENSE = "{{ cookiecutter.license }}"
USE_PYSCN = "{{ cookiecutter.use_pyscn }}" == "yes"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"

SRC = os.path.join("src", PACKAGE_NAME)


def remove(*paths):
    for path in paths:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)


def remove_empty_dirs(root):
    if not os.path.isdir(root):
        return
    for dirpath, _dirnames, _filenames in os.walk(root, topdown=False):
        if not os.listdir(dirpath):
            os.rmdir(dirpath)


# --- project_type: prune the two flavors not selected ---

DATA_SCIENCE_PATHS = [
    "data",
    "notebooks",
    "models",
    "reports",
    os.path.join(SRC, "data"),
    os.path.join(SRC, "features"),
    os.path.join(SRC, "models"),
    os.path.join(SRC, "visualization"),
]

FASTAPI_PATHS = [
    os.path.join(SRC, "main.py"),
    os.path.join(SRC, "api"),
    os.path.join(SRC, "core"),
]

DJANGO_PATHS = [
    "manage.py",
    "config",
    os.path.join(SRC, "apps"),
]

if PROJECT_TYPE != "data_science":
    remove(*DATA_SCIENCE_PATHS)

if PROJECT_TYPE != "fastapi":
    remove(*FASTAPI_PATHS)

if PROJECT_TYPE != "django":
    remove(*DJANGO_PATHS)
else:
    core_app = os.path.join(SRC, "apps", "core")
    if DJANGO_FLAVOR != "drf":
        remove(os.path.join(core_app, "serializers.py"))
    if DJANGO_FLAVOR != "ninja":
        remove(os.path.join(core_app, "api.py"))

# --- docker: only for fastapi/django, and only if requested ---

if PROJECT_TYPE == "data_science" or not USE_DOCKER:
    remove("docker-compose.yml", "Dockerfile", ".env.example")

if PROJECT_TYPE != "fastapi" or not USE_DOCKER:
    remove(os.path.join(SRC, "core", "db.py"))

# --- CI provider: keep only the matching file ---

if CI_PROVIDER != "github":
    remove(os.path.join(".github", "workflows", "ci.yml"))
if CI_PROVIDER != "gitlab":
    remove(".gitlab-ci.yml")
remove_empty_dirs(".github")

# --- license ---

if LICENSE == "None":
    remove("LICENSE")

# --- pyscn ---

if not USE_PYSCN:
    remove(".pyscn.toml")

remove_empty_dirs(SRC)
remove_empty_dirs("src")
