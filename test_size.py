"""
Test Notes instance method size()
File: test_size.py
Inital developers: COMP801 instructors
Developer: Swathi Danturi
Collaborator(s): enter your collaborator(s) name(s): None
Date: 09/30/2024
"""
import pytest
from notes import Notes


def test_size_3():
    """
    Test Notes object with 3 lines
    """
    notes_lst = ['sunny day today', 'need a break?', 'sure!']
    n_obj = Notes(notes_lst)
    actual = n_obj.size()
    expected = 3
    assert actual == expected


def test_size_0():
    """
    Test Notes object with no lines of text
    """
    notes_lst = []
    n_obj = Notes(notes_lst)
    actual = n_obj.size()
    expected = 0
    assert actual == expected


pytest.main()
