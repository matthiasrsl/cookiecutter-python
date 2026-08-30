"""Train a model on the processed dataset and persist it to ``models/``."""

from pathlib import Path

MODELS_DIR = Path("models")


def main() -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
