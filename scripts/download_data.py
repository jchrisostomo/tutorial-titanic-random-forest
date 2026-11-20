"""Download the Titanic competition data from Kaggle into ./data.

Requires a Kaggle API token (~/.kaggle/access_token or KAGGLE_API_TOKEN) and having accepted
the competition rules at https://www.kaggle.com/competitions/titanic.

Usage:
    python scripts/download_data.py
"""
import shutil
import sys
from pathlib import Path

COMPETITION = "titanic"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
REQUIRED_FILES = ["train.csv", "test.csv"]


def data_present() -> bool:
    return all((DATA_DIR / name).exists() for name in REQUIRED_FILES)


def download() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    if data_present():
        print(f"Data already in {DATA_DIR}, skipping download.")
        return

    try:
        import kagglehub
    except ImportError:
        sys.exit("The 'kagglehub' package is not installed. Run: pip install -r requirements.txt")

    print(f"Downloading '{COMPETITION}' ...")
    try:
        cache_dir = Path(kagglehub.competition_download(COMPETITION))
    except Exception as exc:  # missing credentials or rules not accepted
        sys.exit(
            f"Download failed: {exc}\n"
            "Check that your Kaggle credentials are set (~/.kaggle/access_token, "
            "KAGGLE_API_TOKEN, or legacy ~/.kaggle/kaggle.json) and that you accepted "
            "the rules at https://www.kaggle.com/competitions/titanic."
        )

    for csv in cache_dir.glob("*.csv"):
        shutil.copy(csv, DATA_DIR / csv.name)
    print("Done:", ", ".join(sorted(p.name for p in DATA_DIR.glob("*.csv"))))


if __name__ == "__main__":
    download()
