"""Generate figures from the processed dataset into ``reports/figures``."""

from pathlib import Path

FIGURES_DIR = Path("reports/figures")


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
