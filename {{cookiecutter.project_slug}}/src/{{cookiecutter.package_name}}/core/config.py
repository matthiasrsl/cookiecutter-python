from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "{{ cookiecutter.project_name }}"
{% if cookiecutter.use_docker == "yes" %}
    database_url: str = "postgresql://postgres:postgres@db:5432/{{ cookiecutter.package_name }}"
{% endif %}


settings = Settings()
