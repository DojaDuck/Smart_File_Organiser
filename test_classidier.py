import pytest
from app.classifier import classify_file

def test_classify_image():
    file_meta = {
        "extension": "jpg",
        "size": 5000
    }
    assert classify_file(file_meta) == "image"


def test_classify_junk():
    file_meta = {
        "extension": "tmp",
        "size": 2000
    }
    assert classify_file(file_meta) == "junk"

def test_classify_small_file_review():
    file_meta = {
        "extension": "txt",
        "size": 10
    }
    assert classify_file(file_meta) == "review"


def test_classify_unknown():
    file_meta = {
        "extension": "weirdext",
        "size": 5000
    }
    assert classify_file(file_meta) == "unknown"
