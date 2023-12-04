"""
PLEASE fold the word list
"""
import random

english_wordlist = []
with open("englishwords.txt", 'r') as eng:
    for word in eng:
        english_wordlist.append(word.strip())

spanish_wordlist = []


def trim_dictionary_by_word_length(d, num_letters):
    n = []
    for w in d:
        if len(w) == num_letters:
            n.append(w)
    return n


def trim_dictionary_by_letter(d, letter, position=-1):
    n = []
    for w in d:
        if position == -1:
            if letter in w:
                n.append(w)
        else:
            if w[position] == letter:
                n.append(w)
    return n


class Words:
    """
    This class creates an outline for a dictionary.
    """
    def __init__(self, words):
        self.words = words

    def is_word(self, word):
        """
        Checks if a word is a valid word in the dictionary.
        """
        return word in self.words

    def trim_dictionary_by_word_length(self, num_letters):
        """
        Trims a dictionary so that it only has a certain number of letters.
        :param num_letters: (Tuple) The number of letters you would like to trim the dictionary to.
        :return: nothing
        """
        self.words = trim_dictionary_by_word_length(self.words, num_letters)

    def trim_dictionary_by_letter(self, letter, position=-1):
        """
        Trims a dictionary so that it only contains a certain letter,
        as well as a position if specified.
        """
        self.words = trim_dictionary_by_letter(self.words, letter, position)

    def get_random_word(self, word_length=-1, letter=-1, position=-1):
        """
        Grabs a random word from the dictionary.
        """
        new_dict = self.words
        if word_length != -1:
            new_dict = trim_dictionary_by_word_length(new_dict, word_length)
        if letter != -1:
            new_dict = trim_dictionary_by_letter(new_dict, letter, position)
        return random.choice(new_dict)


class EnglishWords(Words):
    """
    Import the entire list of English words and associated methods.
    """
    def __init__(self):
        super().__init__(english_wordlist)


class SpanishWords(Words):
    """
    Import the entire list of Spanish words and associated methods.
    """
    def __init__(self):
        super().__init__(spanish_wordlist)
