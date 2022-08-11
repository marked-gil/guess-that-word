import random
from localStoragePy import localStoragePy
from colorama import init, Fore, Style
from arts import LOGO, MINOR_LOGO
from dictionary import easy_words, hard_words
from word_manager import Word
from score_manager import Scorer
from utility_manager import UtilityTools as utility

# keeps color change within the text inside print statement
init(autoreset=True)


def display_logo(logo):
    """
    Returns the game ascii logo after clearing the terminal
    """
    utility.clear_terminal()
    print(Fore.GREEN + logo)
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
        "        c. Beat the Highscore - guess 15 EASY & HARD words with "
        "scoring\n"
        "     2. A definition will be shown, and you will guess the word it "
        "defines"
        "\n     3. You are allowed 3 attempts to guess the word.\n"
        "     4. Before each attempt, you will be provided with clues:\n"
        "        a. 1st clue = the number of letters in the word\n"
        "        b. 2nd clue = the first and last letters\n"
        "        c. 3rd clue = additional letters within the word"
    )


def show_game_modes():
    """
    Shows the different modes of the game to choose from
    """
    print(utility.blank_lines(1))
    print("GAME MODES:\n".center(80))
    print("[1] Easy Mode      [2] Hard Mode      "
          "[3] Beat the Highscore\n\n".center(80))


def see_howtoplay_input_validator():
    """
    Prompts user to enter 'y' to see the instruction or 'n' to
    proceed to Game Menu, and validates the input.
    Returns user input
    """
    print(utility.blank_lines(3))
    view_instruction = input(Fore.YELLOW + "Enter 'Y' for the instruction; "
                             "or, enter 'N' for Game Menu:\n".center(80) +
                             Style.RESET_ALL).lower()
    while view_instruction not in ('y', 'n'):
        display_logo(LOGO)
        print(utility.blank_lines(2))
        print(Fore.RED + "Wrong input. Please enter 'Y' or 'N' only.".center(80))
        view_instruction = input(Fore.YELLOW + "Enter 'Y' for the instruction; "
                                 "or, enter 'N' for Game Menu:\n"
                                 .center(80) + Style.RESET_ALL).lower()

    return view_instruction


def see_modes_input_validator():
    """
    Prompts user to enter 'y' to go to Game Modes menu, or
    'n' to return home, and validates the input.
    Returns user input
    """
    print(utility.blank_lines(1))
    see_menu = input(Fore.YELLOW + "Enter 'Y' for Game Modes menu; or, enter "
                     "'N' to return home:\n".center(80) + Style.RESET_ALL).lower()
    while see_menu not in ('y', 'n'):
        show_instruction()
        print(Fore.RED + "Invalid input. Please enter 'Y' or 'N' only.".center(80))
        see_menu = input(Fore.YELLOW + "Enter 'Y' for Game Modes menu; or, "
                         "enter 'N' to return home:\n".center(80) + Style.RESET_ALL).lower()

    return see_menu


def play_again_input_validator():
    """
    Prompts user to play again by entering designated input or following the described instruction;
    it validates the user input, provides feedback if input invalid, and refreshes the game if
    input valid.
    """
    play_again_input = input(Fore.YELLOW + "To play again, enter 'Y' or press the 'Run Progran' button at the top.\n".center(80)).lower()
    while play_again_input != 'y':
        utility.clear_terminal()
        print(utility.blank_lines(8))
        if play_again_input == "":
            play_again_input = "a blank input"
        print(Fore.RED + f"You entered '{play_again_input}' which is invalid. Try again!".center(80))
        play_again_input = input(Fore.YELLOW + "To play again, enter 'Y'; or, press the 'Run Progran' button at the top.\n".center(80) + Style.RESET_ALL).lower()
    
    utility.return_home()


def game_mode_input_validator(feedback=None):
    """
    Prompts user to select game mode and validates the input;
    returns the game mode number
    """
    display_logo(LOGO)
    show_game_modes()

    if feedback is not None:
        print(feedback)

    try:
        game_mode_int = int(input(Fore.YELLOW + "Choose a game mode by entering "
                            "'1', '2', or '3':\n".center(80) + Style.RESET_ALL))
    except ValueError:
        message = Fore.RED + "Your input should be a number.".center(80)
        game_mode_int = game_mode_input_validator(message)
    else:
        if game_mode_int not in (1, 2, 3):
            message = Fore.RED + "Your input is out of range.".center(80)
            game_mode_int = game_mode_input_validator(message)

    return game_mode_int


def main():
    """
    Runs the entire gaming program from start to finish
    """
    # HOME <-- start
    display_logo(LOGO)

    # validates if user wants to read instruction
    see_instruction = see_howtoplay_input_validator()
    if see_instruction == 'y':
        show_instruction()
        see_modes = see_modes_input_validator()
        if see_modes == 'y':
            game_mode_num = game_mode_input_validator()
        elif see_modes == 'n':
            utility.clear_terminal()
            utility.return_home()
    elif see_instruction == 'n':
        game_mode_num = game_mode_input_validator()
    # HOME <-- end

    # Play Game <-- start
    utility.clear_terminal()
    play_game(game_mode_num)

    utility.clear_terminal()
    total_right_guesses = Scorer.total_correct_guesses
    print(utility.blank_lines(4))
    print(Fore.MAGENTA + f"You correctly guessed {total_right_guesses} "
          f"word{'s' if total_right_guesses > 1 else ''} "
          "out of 15.\n".center(80))

    if game_mode_num == 3:
        storage_message, localstorage = store_highscore().values()
        print(Fore.YELLOW + storage_message.center(80))
        reset_highscore_validator(localstorage)

    # Asks the user if they want to play again, and validates the input
    play_again_input_validator()
    # Play Game <-- end


if __name__ == '__main__':
    main()
