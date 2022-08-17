import pytest

from main import clean


def test_clean_empty_row():
    assert clean([]) == []


def test_clean_with_whitespace():
    assert clean(["Avatar    ", "Spectre", "John Carter "]) == ["Avatar", "Spectre", "John Carter"]


def test_clean_with_no_whitespace():
    assert clean(["Avatar", "Spectre", "John Carter"]) == ["Avatar", "Spectre", "John Carter"]
