import math
import os
from arts import LOGO, MINOR_LOGO
from dictionary import easy_words, hard_words
from word_manager import Word


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


def display_game_area(word_def, placeholder):
    """
    Displays the game area template and accepts arguments
    for the "word definition" and "word placeholder"
    """
    game_area_template = f"{MINOR_LOGO} {' ' * 30} Score: ___/15\n"\
        + "\n" * 2\
        + "Definition:".center(80)\
        + "\n" * 2\
        + word_def.center(80)\
        + "\n" * 2\
        + '  '.join(placeholder).center(80)\
        + "\n" * 3

    print(game_area_template)


def display_logo(logo):
    """
    Returns the game ascii logo
    """
    return f"{logo} \n {(' ' * 14)} Welcome to the game that will test your vocabulary.\n\n{'=' * 80}"


def play_game(game_mode):
    """
    Runs the main game with specific game mode
    """

    game_on = True

    while game_on:
        os.system('cls||clear')

        if game_mode == 1:
            selected_word = Word(easy_words)
        elif game_mode == 2:
            selected_word = Word(hard_words)
        elif game_mode_num == 3:
            selected_word = Word(easy_words) if len(Word.used_words) < 8 else Word(hard_words)

        word_definition = selected_word.definition
        word_to_guess = selected_word.word.upper()

        word_placeholder = ["___" for _ in range(len(word_to_guess))]
        display_game_area(word_definition, word_placeholder)

        print(f"Used Words Id: {Word.used_words}")

        not_guessed_yet = True
        num_guess = 0

        while not_guessed_yet and num_guess != 3:
            guess = input("Provide your guess:\n".center(80)).upper()

            if guess == word_to_guess:
                os.system('cls||clear')
                not_guessed_yet = False
                display_game_area(word_definition, word_to_guess)
                print("Correct!\n".center(80))
            else:
                num_guess += 1
                if num_guess == 1:
                    os.system('cls||clear')
                    word_placeholder = give_1st_hint(word_to_guess, word_placeholder)
                    display_game_area(word_definition, word_placeholder)
                    print("Here are clues. Try again!\n".center(80))
                elif num_guess == 2:
                    os.system('cls||clear')
                    word_placeholder = give_2nd_hint(word_to_guess, word_placeholder)
                    display_game_area(word_definition, word_placeholder)
                    print("More clues for you. Try again!\n".center(80))
                else:
                    os.system('cls||clear')
                    display_game_area(word_definition, word_to_guess)
                    print("Sorry, you did not guess it!\n".center(80))

        input("Press 'Enter' to proceed to the next word.\n".center(80))


# Home <-- start
print(display_logo(LOGO))
wants_instruction = input("To read the instruction, press 'Y'; otherwise, press 'N' to continue:\n").lower()
# Home <-- end

# validates if user wants to read instruction <-- start
while wants_instruction not in ['y', 'n']:
    wants_instruction = input("Please press 'Y' to read the instruction; or, press 'N' to proceed to the game:\n").lower()

if wants_instruction == 'y':
    os.system('cls||clear')
    print(display_logo(LOGO))
    print(
        "HOW TO PLAY:\n"
        "1. There are 3 modes of the game you can choose to play:\n"
        "   a. Easy Mode - guess 15 EASY words\n"
        "   b. Hard Mode - guess 15 HARD words\n"
        "   c. Beat the Highscore - guess 15 EASY & HARD words with scoring\n"
        "2. You will be presented with a definition, and you need to guess the word that it defines\n"
        "3. You are allowed 3 attempts to guess the word.\n"
        "4. Before each attempt, you will be provided with clues:\n"
        "   a. 1st clue = the number of letters in the word\n"
        "   b. 2nd clue = the first and last letters\n"
        "   c. 3rd clue = additional 1 or 2 letters within the word\n"
    )
    proceed_to_menu = input("To proceed to the game, enter 'Y'; otherwise, enter 'N' to return home:\n")
    while proceed_to_menu not in ['y', 'n']:
        proceed_to_menu = input("Please enter 'Y' to proceed; or 'N' to return home:\n")
elif wants_instruction == 'n':
    os.system('cls||clear')
# validates if user wants to read instruction <-- end

# Game Mode <-- start
if proceed_to_menu == 'y':
    os.system('cls||clear')
    print(display_logo(LOGO))
    print(
        "GAME MODES:\n"
        "  1. Easy Mode\n"
        "  2. Hard Mode\n"
        "  3. Beat the Highscore\n"
        )
elif proceed_to_menu == 'n':
    """should return to home"""
    pass

game_mode_num = int(input("Choose a game mode by entering '1', '2', or '3':\n"))

while game_mode_num not in [1, 2, 3]:
    game_mode_num = input("You need to enter '1', '2', or '3'\n")
# Game Mode <-- end

# Play Game <-- start
os.system('cls||clear')
play_game(game_mode_num)
# Play Game <-- end
