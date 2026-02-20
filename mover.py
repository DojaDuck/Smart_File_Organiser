import shutil
from pathlib import Path
from config import BASE_OUTPUT_DIR, REVIEW_DIR, DUPLICATE_DIR, USELESS_DIR

def ensure_directories():
    BASE_OUTPUT_DIR.mkdir(exist_ok=True)
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    DUPLICATE_DIR.mkdir(parents=True, exist_ok=True)
    USELESS_DIR.mkdir(parents=True, exist_ok=True)

def move_file(file_meta, category):
    destination = BASE_OUTPUT_DIR / category
    destination.mkdir(exist_ok=True)
    target_path = destination / file_meta["path"].name
    shutil.move(str(file_meta["path"]), str(target_path))
  
def move_duplicate(file_meta):
    target_path = DUPLICATE_DIR / file_meta["path"].name
    shutil.move(str(file_meta["path"]), str(target_path))

def move_useless(file_meta):
    target_path = USELESS_DIR / file_meta["path"].name
    shutil.move(str(file_meta["path"]), str(target_path))
