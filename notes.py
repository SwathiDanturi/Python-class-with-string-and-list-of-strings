"""
More practice with modules and application of Python class concept, string,
and list of strings with a given structre (words separated by white spaces).
File: notes.py
Initial developers: COMP 801 instructors
Developer: Swathi Danturi
Collaborator(s): None
Date: 09/30/2024
"""


class Notes:
    """
    Ecapsulate notes processing.
    Instance variable: `self.notes` of type list of strings, where a string
        represents words separated by white spaces.
        Example: ['good stories', 'have', 'a good plot']
    """

    def __init__(self, notes: list):
        """
        Create and initialize Notes object with `notes` value.
        :param notes: list of strings separated by white spaces
        """
        self.notes = notes

    def size(self) -> int:
        """
        Return how many elements in `self.notes`
        """
        return len(self.notes)

    @staticmethod
    def how_often_word(sentence):
        """
        Find out how often each word appears in `sentence`.
        :param sentence: string of words separate by white spaces
        :return: dictionary
            keys: unique words in `sentence`
            values: integers, how often corresponding key appears in `sentence`
        """

    def word_histogram(self):
        """
        Find out how often each word appears in `self.notes`.
        :return: dictionary
            keys: unique words in `sentence`
            values: integers, how often corresponding key appears in `sentence`

        Implementation requirement: use `how_often_word()`
        """
