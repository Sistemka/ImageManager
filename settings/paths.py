from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGES_DIR = Path(BASE_DIR, 'images2')
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR = IMAGES_DIR.as_posix()
