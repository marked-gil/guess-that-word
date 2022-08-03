"""
This module contains the class that provide a randomly selected
word that will be used in the game
"""
from random import choice


class Word:
    """
    Provides a word instance that will be guessed in the game
    """
    used_words = []    # Holds the IDs of used words

    def __init__(self, words_dict):
        self.random_word = self._get_random_word(words_dict)
        Word.used_words.append(self.random_word[0])

    def _get_random_word(self, words_dict):
        """
        Selects a random word from passed in words dictionary
        and returns a tuple of word/definition and id
        """
        word_id = choice(list(words_dict.keys()))
        while word_id in Word.used_words:
            word_id = choice(list(words_dict.keys()))
        return word_id, words_dict[word_id]
