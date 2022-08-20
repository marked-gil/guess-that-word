"""
This file runs the main() function which contains the entire program
from start to finish.
"""
from colorama import init, Fore, Style
from arts import LOGO
from game_manager import Game
from score_manager import Scorer
from utility_manager import clear_terminal, blank_lines, return_home

# keeps color change within the text inside print statement
init(autoreset=True)


def display_logo(logo):
    """
    Displays the ascii logo after clearing the terminal
    """
    clear_terminal()
    print(Fore.GREEN + logo)
    print("Welcome to the game that will test your vocabulary.\n".center(80))
    print(('=' * 70).center(80))


def show_instruction():
    """
    Displays the game mechanics with logo on top
    """
    display_logo(LOGO)
    print(
        "     HOW TO PLAY:\n"
        "     1. There are 3 modes of the game you can choose to play:\n"
        "        a. Easy Mode - guess 15 EASY words\n"
        "        b. Hard Mode - guess 15 HARD words\n"
        "        c. Beat the High Score - guess 15 EASY & HARD words with "
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
    Displays the different modes of the game
    """
    print(blank_lines(1))
    print("GAME MODES:\n".center(80))
    print("[1] Easy Mode      [2] Hard Mode      "
          "[3] Beat the High Score\n\n".center(80))


def show_scoring_system(mode):
    """
    Displays the scoring system of the 'Beat the High Score' game mode
    """
    if mode == 3:
        display_logo(LOGO)
        print(blank_lines(2))
        print("In the 'Beat the High Score' mode, you earn:".center(80))
        print(blank_lines(1))
        print("5 points -- if guess is correct on the 1st try".center(80))
        print("3 points -- if guess is correct on the 2nd try".center(80))
        print("1 point -- if guess is correct on the 3rd try".center(80))
        print(blank_lines(1))


def start_hiscore_input_validator(mode):
    """
    Prompts user to proceed to 'Beat the High Score' game; validates
    user input, and flashes feedback message if invalid.
    Parameter: game mode number
    """
    if mode == 3:
        try:
            start_game = input(Fore.YELLOW + "Are you ready? Enter Y to "
                               "proceed, or N to return home.\n".center(80) +
                               Style.RESET_ALL).lower()
            if start_game not in ('y', 'n'):
                raise ValueError("Invalid input. Enter Y or N only.")
        except ValueError as err:
            display_logo(LOGO)
            show_scoring_system(mode)
            print(Fore.RED + str(err).center(80))
            start_hiscore_input_validator(mode)

        # refreshes the program
        if start_game == 'n':
            return_home()


def see_howtoplay_input_validator():
    """
    Prompts user to enter Y to see the instruction, or N to proceed to
    Game Modes menu; validates the user input and flashes feedback
    message if invalid.
    Returns: user input [Y or N]
    """
    print(blank_lines(3))
    view_instruction = input(Fore.YELLOW + "Enter Y for the instruction; "
                             "or, enter N for Game Modes menu:\n".center(80) +
                             Style.RESET_ALL).lower()

    while view_instruction not in ('y', 'n'):
        display_logo(LOGO)
        print(blank_lines(2))
        print(Fore.RED + "Invalid input. Please enter Y or N only."
              .center(80))
        view_instruction = input(Fore.YELLOW + "Enter Y for the instruction;"
                                 " or, enter N for Game Modes menu:\n"
                                 .center(80) + Style.RESET_ALL).lower()
    return view_instruction


def see_modes_input_validator():
    """
    Prompts user to enter Y to go to Game Modes menu, or N to return home;
    validates the user input, and flashes a feedback message if invalid.
    Returns: user input [Y or N]
    """
    print(blank_lines(1))
    see_menu = input(Fore.YELLOW + "Enter Y for Game Modes menu; or, enter "
                     "N to return home:\n".center(80) +
                     Style.RESET_ALL).lower()

    while see_menu not in ('y', 'n'):
        show_instruction()
        print(Fore.RED + "Invalid input. Please enter Y or N "
              "only.".center(80))
        see_menu = input(Fore.YELLOW + "Enter Y for Game Modes menu; or, "
                         "enter N to return home:\n".center(80) +
                         Style.RESET_ALL).lower()
    return see_menu


def play_again_input_validator():
    """
    Prompts user to play again; validates user input, and flashes feedback
    message if input invalid. If input valid, game is refreshed.
    """
    try:
        play_again_input = input(Fore.YELLOW + "To play again, enter Y; or, "
                                 "click the 'Run Program' button at the top."
                                 "\n".center(80) +
                                 Style.RESET_ALL).lower()
        if play_again_input not in ('y', 'n'):
            raise ValueError("Invalid input. Please enter Y only.")
    except ValueError as err:
        clear_terminal()
        print(blank_lines(9))
        print(Fore.RED + str(err).center(80))
        play_again_input_validator()
    else:
        return_home()


def game_mode_input_validator(feedback=None):
    """
    Prompts user to select game mode and validates their input; flashes
    feedback message if input invalid.
    Returns: game mode number
    """
    display_logo(LOGO)
    show_game_modes()

    # displays the passed in feedback message
    if feedback is not None:
        print(feedback)

    # displays the prompt, and validates input with error handling
    try:
        game_mode_int = int(input(Fore.YELLOW + "Choose a game mode by "
                                  "entering 1, 2, or 3:\n".center(80) +
                                  Style.RESET_ALL))
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
    # ******* HOME [start] *******
    display_logo(LOGO)

    # checks if user wants to read instruction, and validates input
    see_instruction = see_howtoplay_input_validator()

    if see_instruction == 'y':
        show_instruction()
        see_modes = see_modes_input_validator()
        if see_modes == 'y':
            # shows game modes menu and validates user input
            game_mode_num = game_mode_input_validator()
            # run only on 'Beat the High Score' mode
            show_scoring_system(game_mode_num)
            start_hiscore_input_validator(game_mode_num)
        elif see_modes == 'n':
            # refreshes script
            clear_terminal()
            return_home()

    elif see_instruction == 'n':
        # shows game modes menu and validates user input
        game_mode_num = game_mode_input_validator()
        # run only on 'Beat the High Score' mode
        show_scoring_system(game_mode_num)
        start_hiscore_input_validator(game_mode_num)
    # ******* HOME [end] *******

    # ******* MAIN GAME [start] *******
    game = Game(game_mode_num)
    clear_terminal()
    game.play_game()
    # ******* MAIN GAME [end] *******

    # ******* USER PERFORMANCE [start] *******
    score_msg = Scorer.show_performance(game_mode_num)

    # store high score if on game mode 3
    if game_mode_num == 3 and Scorer.total_score != 0:
        Scorer.store_highscore()
        Scorer.validate_to_reset_highscore(score_msg)
    # ******* USER PERFORMANCE [end] *******

    # prompts user to play again, and validates user input
    print(blank_lines(2))
    play_again_input_validator()


if __name__ == '__main__':
    main()
