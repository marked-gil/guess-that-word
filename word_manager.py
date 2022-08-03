"""
This module contains the class that provide a randomly selected
word that will be used in the game
"""
from random import choice


class Word:
    """
    Creates a word instance that will be guessed in the game
    """
    used_words = []    # Holds the IDs of used words

    def __init__(self, words_list):
        self.word_obj = self._get_random_word(words_list)
        self.word = self.word_obj["word"]
        self.definition = self.word_obj["definition"]
        self.word_id = self.word_obj["id"]
        Word.used_words.append(self.word_id)

    def _get_random_word(self, words_list):
        """
        Selects a random word from passed in words dictionary
        and returns a tuple of word/definition and id
        """
        word_obj = choice(words_list)
        word_id = word_obj["id"]

        while word_id in Word.used_words:
            word_id = word_obj["id"]

        return word_obj
