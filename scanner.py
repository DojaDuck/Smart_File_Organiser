import os
from pathlib import Path

def scan_directory(path):
    files = []
    for root, _, filenames in os.walk(path):
        for name in filenames:
            full_path = Path(root) / name
            try:
                stat = full_path.stat()
                files.append({
                    "path": full_path,
                    "size": stat.st_size,
                    "extension": full_path.suffix.lower().replace(".", "")
                })
            except Exception:
                continue
    return files
