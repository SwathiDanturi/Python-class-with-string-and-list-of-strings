"""
Test Notes instance method word_histogram()
File: test_word_histogram.py
Developer: Swathi Danturi
Collaborator(s): enter your collaborator(s) name(s): None
Date: 09/30/2024
"""

import pytest
from notes import Notes


def test_word_histogram_with_repetitive_words():
    """
    Test Notes instance method how_often_word() with repetitive words
    """
    notes_obj = Notes(["This", "is", "a", "test", "This", "is", "test"])
    expected = {'This': 2, 'is': 2, 'a': 1, 'test': 2}
    actual = notes_obj.test_word_histogram()
    assert actual == expected


def test_word_histogram_without_repetitive_words():
    """
    Test Notes instance method how_often_word() with unique words
    """
    notes_obj = Notes(["Print", "my", "unique", "dictionary"])
    expected = {'Print': 1, 'my': 1, 'unique': 1, 'dictionary': 1}
    actual = notes_obj.test_word_histogram()
    assert actual == expected


pytest.main()
