import tempfile
from pathlib import Path
from app.duplicate_detector import detect_duplicates

def test_detect_duplicates():
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = Path(tmpdir) / "file1.txt"
        file2 = Path(tmpdir) / "file2.txt"

        content = "duplicate content"

        file1.write_text(content)
        file2.write_text(content)

        files = [
            {"path": file1},
            {"path": file2}
        ]

        duplicates = detect_duplicates(files)

        assert len(duplicates) == 1
        assert duplicates[0]["path"] == file2
