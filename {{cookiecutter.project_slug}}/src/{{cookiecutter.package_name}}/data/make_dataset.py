"""Scripts to turn raw data (in ``data/raw``) into a processed dataset."""

from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
