import shutil
from pathlib import Path

import kagglehub


DATASET_NAME = "msambare/fer2013"
TARGET_DIR = Path("data/raw/fer2013")


def main():
    path = Path(kagglehub.dataset_download(DATASET_NAME))
    TARGET_DIR.parent.mkdir(parents=True, exist_ok=True)

    if TARGET_DIR.exists():
        print(f"Dataset already exists at: {TARGET_DIR}")
        return

    shutil.copytree(path, TARGET_DIR)
    print(f"Dataset copied to: {TARGET_DIR}")


if __name__ == "__main__":
    main()