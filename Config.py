from pathlib import Path

BASE_OUTPUT_DIR = Path("organized_output")
REVIEW_DIR = BASE_OUTPUT_DIR / "review"
DUPLICATE_DIR = REVIEW_DIR / "duplicates"
USELESS_DIR = REVIEW_DIR / "useless"

FILE_TYPE_MAP = {
    "image": ["jpg", "jpeg", "png", "gif", "bmp"],
    "documents": ["pdf", "doc", "docx", "txt", "xls", "xlsx"],
    "videos": ["mp4", "mov", "avi", "mkv"],
    "audio": ["mp3", "wav"],
    "archives": ["zip", "rar", "7z", "tar", "gz"],
    "code": ["py", "js", "java", "cpp", "c", "html", "css"],
}

JUNK_EXTENSIONS = ["tmp", "log", "bak"]

MIN_FILE_SIZE_BYTES = 1024  # < 1KB considered low value
