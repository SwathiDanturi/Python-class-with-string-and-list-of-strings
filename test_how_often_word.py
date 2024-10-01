"""
Test Notes instance method how_often_word()
File: test_how_often_word.py
Developer: Swathi Danturi
Collaborator(s): enter your collaborator(s) name(s): None
Date: 09/30/2024
"""

import pytest
from notes import Notes


def test_how_often_word_with_repetitive_words():
    """
    Test Notes instance method how_often_word() with repetitive words
    """
    test_sentence = "This is a test sentence This is a test This is a This is This"
    expected = {'This': 5, 'is': 4, 'a': 3, 'test': 2, 'sentence': 1}
    actual = Notes.how_often_word(test_sentence)
    assert actual == expected


def test_how_often_word_without_repetitive_words():
    """
    Test Notes instance method how_often_word() with unique words
    """
    test_sentence = "Print my unique dictionary"
    expected = {'Print': 1, 'my': 1, 'unique': 1, 'dictionary': 1}
    actual = Notes.how_often_word(test_sentence)
    assert actual == expected


pytest.main()