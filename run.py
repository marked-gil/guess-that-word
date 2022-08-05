import os
import sys
import random
from arts import LOGO, MINOR_LOGO
from dictionary import easy_words, hard_words
from word_manager import Word


def clear_terminal():
    """
    Clears the terminal
    """
    print("\033c")


def display_logo(logo):
    """
    Returns the game ascii logo
    """
    clear_terminal()
    print(logo)
    print("Welcome to the game that will test your vocabulary.\n".center(80))
    print(('=' * 70).center(80))


def show_instruction():
    """
    Shows the game mechanics
    """
    display_logo(LOGO)
    print(
        "     HOW TO PLAY:\n"
        "     1. There are 3 modes of the game you can choose to play:\n"
        "        a. Easy Mode - guess 15 EASY words\n"
        "        b. Hard Mode - guess 15 HARD words\n"
        "        c. Beat the Highscore - guess 15 EASY & HARD words with scoring\n"
        "     2. A definition will be shown, and you will guess the word it defines"
        "\n     3. You are allowed 3 attempts to guess the word.\n"
        "     4. Before each attempt, you will be provided with clues:\n"
        "        a. 1st clue = the number of letters in the word\n"
        "        b. 2nd clue = the first and last letters\n"
        "        c. 3rd clue = additional letters within the word\n"
    )


def show_game_modes():
    """
    Shows the different modes of the game to choose from
    """
    print(
        "GAME MODES:\n"
        "  1. Easy Mode\n"
        "  2. Hard Mode\n"
        "  3. Beat the Highscore\n"
        )


def see_instruction_validator():
    """
    Prompts user to enter 'y' to see the instruction or 'n' to
    proceed to Game Menu, and validates the input.
    Returns user input
    """
    view_instruction = input("Enter 'Y' for the instruction; or, enter 'N' for Game Menu:\n".center(80)).lower()
    while view_instruction not in ('y', 'n'):
        display_logo(LOGO)
        view_instruction = input("Enter 'Y' for the instruction; or, enter 'N' for Game Menu:\n".center(80)).lower()

    return view_instruction


def see_modes_validator():
    """
    Prompts user to enter 'y' to go to Game Modes menu, or
    'n' to return home, and validates the input.
    Returns user input
    """
    see_menu = input("Enter 'Y' for Game Modes menu; or, enter 'N' to return home:\n".center(80)).lower()
    while see_menu not in ('y', 'n'):
        show_instruction()
        see_menu = input("Enter 'Y' for Game Modes menu; or, enter 'N' to return home:\n".center(80)).lower()
    
    return see_menu


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
    Gives hint by adding letters to the placeholder, and
    returns the modified placeholder
    """
    indx_list = []
    num_characters = len(word)
    if num_characters < 8:
        while len(indx_list) != 2:
            indx = random.randrange(1, num_characters-1)
            if indx not in indx_list:
                indx_list.append(indx)
    elif num_characters >= 8:
        while len(indx_list) != 3:
            indx = random.randrange(1, num_characters-1)
            if indx not in indx_list:
                indx_list.append(indx)
        placeholder[indx_list[2]] = word[indx_list[2]]

    placeholder[indx_list[0]] = word[indx_list[0]]
    placeholder[indx_list[1]] = word[indx_list[1]]

    return placeholder


def display_game_area(word_def, total_answered, highscore_mode=False, score=0):
    """
    Displays the game area template and accepts arguments for the
    "word definition", "total correct guesses", "boolean for highscore_mode",
    and "score"
    """
    if highscore_mode is True:
        score_display = f'Score: {score}'
        space_between = " " * 15
    else:
        score_display = ""
        space_between = " " * 30

    total_words = len(Word.used_words)
    game_area_template = f"{MINOR_LOGO} {space_between} {score_display}      Correct Answers: {total_answered} of {total_words}\n"\
        + "\n" * 2\
        + "Definition:".center(80)\
        + "\n" * 2\
        + word_def.center(80)\
        + "\n" * 2\

    return game_area_template


def display_placeholder(placeholder):
    """
    Displays the placeholder for the word
    """
    word_placeholder = '  '.join(placeholder).center(80)\
        + "\n" * 3

    print(word_placeholder)


def scoring(num_of_guesses):
    """
    Returns the points earned per correctly guessed word
    for game mode 3 (Beat Your Highscore)
    """
    if num_of_guesses == 1:
        points = 5
    elif num_of_guesses == 2:
        points = 3
    elif num_of_guesses == 3:
        points = 1
    else:
        points = 0

    return points


def game_mode_validator():
    """
    Prompts user to select game mode and validates the input;
    returns the game mode number
    """
    clear_terminal()
    display_logo(LOGO)
    show_game_modes()

    try:
        game_mode_int = int(input("Choose a game mode by entering '1', '2', or '3':\n".center(80)))
    except ValueError:
        game_mode_int = game_mode_validator()
    else:
        if game_mode_int not in (1, 2, 3):
            game_mode_int = game_mode_validator()

    return game_mode_int


def game_mode_assembler(mode: int, answered_words: int, score: int):
    """
    Returns the "word object", and "game area" while accepting parameters such as:
    "game mode" (mode), "total of correctly answered words" (answered_words), and "score"
    """
    if mode == 1:
        random_word = Word(easy_words)
    elif mode == 2:
        random_word = Word(hard_words)
    elif mode == 3:
        random_word = Word(easy_words) if len(Word.used_words) < 8 else Word(hard_words)

    if mode in (1, 2):
        return {"word_obj": random_word, "game_area": display_game_area(random_word.definition, answered_words)}

    return {"word_obj": random_word, "game_area": display_game_area(random_word.definition, answered_words, True, score)}


def play_game(game_mode):
    """
    Runs the main game with specific game mode
    """
    game_on = True
    correct_guesses = 0
    score = 0

    while game_on:
        clear_terminal()

        game_object = game_mode_assembler(game_mode, correct_guesses, score)
        word_to_guess = game_object["word_obj"].word.upper()
        word_placeholder = game_object["word_obj"].placeholder

        print(game_object["game_area"])
        display_placeholder(word_placeholder)

        # print(f"Used Words Id: {Word.used_words}")

        not_guessed_yet = True
        num_guess = 0

        while not_guessed_yet and num_guess != 3:
            guess = input("Provide your guess:\n".center(80)).upper()

            num_guess += 1
            if guess == word_to_guess:
                clear_terminal()
                not_guessed_yet = False
                correct_guesses += 1
                score += scoring(num_guess)
                print(game_object["game_area"])
                display_placeholder(word_to_guess)
                print("Correct!\n".center(80))
            else:
                if num_guess == 1:
                    clear_terminal()
                    word_placeholder = give_1st_hint(word_to_guess, word_placeholder)
                    print(game_object["game_area"])
                    display_placeholder(word_placeholder)
                    print("Here are clues. Try again!\n".center(80))
                elif num_guess == 2:
                    clear_terminal()
                    word_placeholder = give_2nd_hint(word_to_guess, word_placeholder)
                    print(game_object["game_area"])
                    display_placeholder(word_placeholder)
                    print("More clues for you. Try again!\n".center(80))
                else:
                    clear_terminal()
                    print(game_object["game_area"])
                    display_placeholder(word_to_guess)
                    print("Sorry, you did not guess it!\n".center(80))

        # Game ends after 15 words
        if len(Word.used_words) == 15:
            game_on = False
        else:
            proceed = input("Press 'Enter' to proceed to the next word:\n".center(80))
            while proceed != "":
                clear_terminal()
                print(game_object["game_area"])
                display_placeholder(word_to_guess)
                proceed = input("Press 'Enter' to proceed to the next word:\n".center(80))


# Home <-- start
display_logo(LOGO)
# Home <-- end

# validates if user wants to read instruction <-- start
see_instruction = see_instruction_validator()
if see_instruction == 'y':
    show_instruction()
    see_modes = see_modes_validator()
    if see_modes == 'y':
        game_mode_num = game_mode_validator()
    elif see_modes == 'n':
        clear_terminal()
        # return home
        os.execv(sys.executable, ['python'] + sys.argv)

elif see_instruction == 'n':
    game_mode_num = game_mode_validator()
# validates if user wants to read instruction <-- end

# Play Game <-- start
clear_terminal()
play_game(game_mode_num)
print("The End!")
# Play Game <-- end
