"""
Demonstrate functionality of the Paragraph class.
File: src/client.py
Initial developers: COMP 801 instructors
Developer: Swathi Danturi
Collaborator(s): None
Date: 09/30/2024
"""
from notes import Notes


def main():
    """
    Demo Notes functionality
    """
    notes_lst = ['sunny day today!', 'need a break', 'going for a walk']
    n_obj = Notes(notes_lst)
    n_count = n_obj.size()
    print(f'Notes count: {n_count}')

    # create another Notes object and find out something else about it.
    print(f'Word Histogram: {n_obj.word_histogram()}')

    notes_sentence = "write test methods and write test cases"
    print(f'How often Word: {Notes.how_often_word(notes_sentence)}')


main()
