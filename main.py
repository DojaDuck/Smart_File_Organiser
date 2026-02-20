import argparse
from scanner import scan_directory
from classifier import classify_file
from duplicate_detector import detect_duplicates
from mover import ensure_directories, move_file, move_duplicate, move_useless
from interactive import review_file
from logger import log

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("path", help="Path to organize")
    args = parser.parse_args()

    ensure_directories()

    files = scan_directory(args.path)
    duplicates = detect_duplicates(files)

    for dup in duplicates:
        move_duplicate(dup)
        log(f"Duplicate moved: {dup['path']}")

    for file in files:
        if file in duplicates:
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
            else:
                continue

        elif category == "unknown":
            decision = review_file(file)
            if decision == "k":
                move_file(file, "misc")
            elif decision == "d":
                file["path"].unlink()

        else:
            move_file(file, category)
            log(f"Moved: {file['path']} → {category}")

    print("\nOrganization complete.")

if __name__ == "__main__":
    main()
