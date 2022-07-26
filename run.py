from random import random
import math

LOGO = """\n
    ╔═══╗────────────╔════╦╗────╔╗─╔╗╔╗╔╗──────╔╗
    ║╔═╗║────────────║╔╗╔╗║║───╔╝╚╗║║║║║║──────║║
    ║║─╚╬╗╔╦══╦══╦══╗╚╝║║╚╣╚═╦═╩╗╔╝║║║║║╠══╦═╦═╝║
    ║║╔═╣║║║║═╣══╣══╣──║║─║╔╗║╔╗║║─║╚╝╚╝║╔╗║╔╣╔╗║
    ║╚╩═║╚╝║║═╬══╠══║──║║─║║║║╔╗║╚╗╚╗╔╗╔╣╚╝║║║╚╝║
    ╚═══╩══╩══╩══╩══╝──╚╝─╚╝╚╩╝╚╩═╝─╚╝╚╝╚══╩╝╚══╝
"""

# Dictionary of words to guess
WORDS_DICTIONARY = {
    1: {
        "word": "empathy",
        "definition": "The action of understanding and vicariously experiencing the feelings, thoughts, and experience of another"
    },
    2: {
        "word": "expatriate",
        "definition": "To leave one's native country to live elsewhere",
    },
    3: {
        "word": "meticulous",
        "definition": "Marked by extreme or excessive care in the consideration or treatment of details",
    },
    4: {
        "word": "intuition",
        "definition": "An innate sense of what is true or what will happen",
    },
    5: {
        "word": "warehouse",
        "definition": "A structure or room for the storage of merchandise or commodities",
    },
    6: {
        "word": "bailiwick",
        "definition": "The sphere in which one has superior knowledge or authority",
    },
    7: {
        "word": "magazine",
        "definition": "A print periodical containing miscellaneous pieces",
    },
    8: {
        "word": "fascism",
        "definition": "A tendency toward or actual exercise of strong autocratic or dictatorial control",
    },
    9: {
        "word": "community",
        "definition": "A unified body of individuals",
    },
    10: {
        "word": "swindle",
        "definition": "To obtain money or property by fraud or deceit",
    },
}


def get_random_word():
    """
    Gets a random word from the words dictionary and return it
    """
    word_id = math.floor((random() * len(WORDS_DICTIONARY)+1))
    return WORDS_DICTIONARY[word_id]


print(LOGO)
print(get_random_word())
