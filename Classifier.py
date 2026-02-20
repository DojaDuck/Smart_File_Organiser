from config import FILE_TYPE_MAP, JUNK_EXTENSIONS, MIN_FILE_SIZE_BYTES

def classify_file(file_meta):
    ext = file_meta["extension"]
    size = file_meta["size"]

    if ext in JUNK_EXTENSIONS:
        return "junk"

    if size < MIN_FILE_SIZE_BYTES:
        return "review"

    for category, extensions in FILE_TYPE_MAP.items():
        if ext in extensions:
            return category

    return "unknown"
