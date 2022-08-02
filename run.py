from random import random
import math
from arts import LOGO
from dictionary import WORDS_DICTIONARY


def get_random_word(used_words_list):
    """
    Gets a random word from the words dictionary while preventing used words
    from being repeated, and returns a tuple of word/definition and id
    """
    word_id = math.floor((random() * len(WORDS_DICTIONARY)+1))
    while word_id in used_words_list:
        word_id = math.floor((random() * len(WORDS_DICTIONARY)+1))
    return WORDS_DICTIONARY[word_id], word_id


def display_placeholder(placeholder, full_answer=False):
    """
    Displays the random word placeholder in the terminal, and
    accepts a boolean argument on whether the full answer is
    to be shown or not
    """
    if full_answer:
        print('   '.join(placeholder))
    else:
        print('  '.join(placeholder))


def give_1st_hint(word, placeholder):
    """
    Gives hint by adding the first and last letters of the word to
    the placeholder and returns the modified placeholder
    """
    first_letter = word[0]
    last_letter = word[-1]
    placeholder[0] = first_letter
    placeholder[-1] = last_letter
    return placeholder


def give_2nd_hint(word, placeholder):
    """
    Gives hint by adding the 2nd and middle letters of the word to
    the placeholder and returns the modified placeholder
    """
    second_letter = word[1]
    middle_letter = word[math.floor(len(word) / 2)]
    placeholder[1] = second_letter
    placeholder[math.floor(len(word) / 2)] = middle_letter
    return placeholder


def show_answer(word, placeholder):
    """
    Displays the correct answer by replacing the placeholder underscores
    with the correct letters and returns the modified placeholder
    """
    for ind, letter in enumerate(word):
        placeholder[ind] = letter
    return placeholder


print(LOGO)

# Holds the IDs of used words
used_words = []

game_on = True

while game_on:
    dictionary_item = get_random_word(used_words)
    used_words.append(dictionary_item[1])
    word_definition = dictionary_item[0]['definition']
    word_to_guess = dictionary_item[0]['word'].upper()

    print(f"Definition:\n\"{word_definition}\"")

    word_placeholder = ["___" for _ in range(len(word_to_guess))]
    print('  '.join(word_placeholder))

    not_guessed_yet = True
    num_guess = 0

    while not_guessed_yet and num_guess != 3:
        guess = input("Provide your guess:\n").upper()

        if guess == word_to_guess:
            not_guessed_yet = False
            print("Congratulations!")
        else:
            num_guess += 1
            if num_guess == 1:
                word_placeholder = give_1st_hint(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder)
                print("Try again!")
            elif num_guess == 2:
                word_placeholder = give_2nd_hint(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder)
                print("Try again!")
            else:
                print("Sorry your guess is wrong!")
                answer = show_answer(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder, True)

    if len(used_words) == 10:
        print("GAME OVER!")
        game_on = False