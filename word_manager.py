"""
This module contains the class Word that provides an instance
that randomly selects a word, and has attributes related to
selected the word.
"""
from random import choice


class Word:
    """
    Creates an instance that randomly selects a word; and it has
    attributes which includes the definition, id, word length, and
    its placeholder. It also tracks the words that are used in the game.
    """
    used_words = []    # Holds the IDs of used words

    def __init__(self, words_list):
        self.word_obj = self._get_random_word(words_list)
        self.word = self.word_obj["word"]
        self.definition = self.word_obj["definition"]
        self.word_id = self.word_obj["id"]
        self.length = len(self.word)
        self.placeholder = ["___" for _ in range(self.length)]
        Word.used_words.append(self.word_id)

    def _get_random_word(self, words_list):
        """
        Randomly selects a word from a list of words dictionary.
        Parameter: words_list
        Returns: word object (a dictionary containing the word, its id, and
        definition)
        """
        word_obj = choice(words_list)

        while word_obj["id"] in Word.used_words:
            word_obj = choice(words_list)

        return word_obj
