import argparse
from app.scanner import scan_directory
from app.classifier import classify_file
from app.duplicate_detector import detect_duplicates
from app.mover import ensure_directories, move_file, move_duplicate, move_useless
from app.interactive import review_file
from app.logger import log

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("path", help="Path to organize")
    args = parser.parse_args()

    ensure_directories()

    files = scan_directory(args.path)
    duplicates = detect_duplicates(files)

    duplicate_paths = {dup["path"] for dup in duplicates}

    # Move duplicates first
    for dup in duplicates:
        move_duplicate(dup)
        log(f"Duplicate moved: {dup['path']}")

    for file in files:
        if file["path"] in duplicate_paths:
            continue

        category = classify_file(file)

        if category == "junk":
            move_useless(file)
            log(f"Junk moved: {file['path']}")

        elif category == "review":
            decision = review_file(file)

            if decision == "d":
                file["path"].unlink()
                log(f"Deleted: {file['path']}")

            elif decision == "k":
                move_file(file, "kept")
                log(f"Kept: {file['path']}")

        elif category == "unknown":
            decision = review_file(file)

            if decision == "k":
                move_file(file, "misc")
                log(f"Moved unknown file: {file['path']}")

            elif decision == "d":
                file["path"].unlink()
                log(f"Deleted unknown file: {file['path']}")

        else:
            move_file(file, category)
            log(f"Moved: {file['path']} → {category}")

    print("\nOrganization complete.")

if __name__ == "__main__":
    main()
