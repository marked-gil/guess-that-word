import random
from localStoragePy import localStoragePy
from colorama import init, Fore, Style
from arts import LOGO, MINOR_LOGO
from dictionary import easy_words, hard_words
from word_manager import Word
from score_manager import Scorer
from utility_manager import UtilityTools

# keeps color change within the text inside print statement
init(autoreset=True)

utility = UtilityTools()


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
        print(Fore.RED + "Wrong input. Please enter 'Y' or 'N' only.".center(80))
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


def display_game_area(word_def, game_mode):
    """
    Displays the game area template and accepts arguments for the
    "word definition", "total correct guesses", "boolean for highscore_mode",
    and "score"
    """
    if game_mode == 3:
        score_display = f"Score: {Scorer.total_score}"
        space = " " * 16
    else:
        score_display = f"Correct Answer: {Scorer.total_correct_guesses}"
        space = " " * 6

    total_words = len(Word.used_words)
    game_area_template = f"\n {Fore.GREEN + MINOR_LOGO} {space}\
    {score_display}        Words Left: {15 - total_words}\n"\
        + Style.RESET_ALL + "=" * 80\
        + utility.blank_lines(2, "inline")\
        + "Definition:".center(80)\
        + utility.blank_lines(1, "inline")\
        + word_def.center(80)\
        + utility.blank_lines(2, "after_line")\

    return game_area_template


def display_placeholder(placeholder):
    """
    Displays the placeholder for the word
    """
    word_placeholder = '  '.join(placeholder).center(80)\
        + utility.blank_lines(3, "after_line")

    print(Fore.CYAN + word_placeholder)


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


def game_mode_assembler(mode: int):
    """
    Returns the "word object", and "game area" while accepting
    the "game mode" (mode) as argument.
    """
    if mode == 1:
        random_word = Word(easy_words)
    elif mode == 2:
        random_word = Word(hard_words)
    elif mode == 3:
        random_word = Word(easy_words) if len(Word.used_words) < 8 \
            else Word(hard_words)

    if mode in (1, 2):
        return {"word_obj": random_word, "game_area":
                display_game_area(random_word.definition, mode)}

    return {"word_obj": random_word, "game_area":
            display_game_area(random_word.definition, mode)}


def store_highscore():
    """
    Stores the highscore in the localStorage, and returns "message"
    (about user's score and/or highscore) and the "local storage"
    """
    u_score = Scorer.total_score
    local_storage = localStoragePy('guessthatword-hiscore')
    hi_score = local_storage.getItem("hi-score")
    message = ""
    if hi_score is None:
        local_storage.setItem("hi-score", u_score)
        hi_score = local_storage.getItem("hi-score")
        message = f"Your score is: {u_score}.\n"
    elif int(hi_score) > u_score:
        message = f"Your score is: {u_score} || the HIGHSCORE is {hi_score}.\n"
    elif int(hi_score) < u_score:
        local_storage.setItem("hi-score", u_score)
        hi_score = local_storage.getItem("hi-score")
        message = "Congratulations! You've just set the NEW HIGHSCORE: "\
            + hi_score
    return {"store_message": message, "local_storage": local_storage}


def reset_highscore_validator(storage_name):
    """
    Prompts user to choose whether to reset highscore or not,
    and validates the input.
    """
    while True:
        clear_hi_score = input("Do you want to reset the highscore? "
                               "['Y' | 'N']:\n".center(80)).lower()
        if clear_hi_score == 'y':
            storage_name.removeItem("hi-score")
            utility.clear_terminal()
            print(
                utility.blank_lines(6) +
                "Highscore reset!".center(80) +
                utility.blank_lines(2, "after_line")
                )
            break
        if clear_hi_score == 'n':
            utility.clear_terminal()
            print(utility.blank_lines(8))
            break

        utility.clear_terminal()
        print(
            utility.blank_lines(8) +
            Fore.RED + "[Enter only 'Y' for Yes, or 'N' for No]".center(80)
            )


def feedback_to_wrong_guess(guess_num, placeholder, word, game_zone, user_guess):
    """
    Responds to every wrong guess by the user by providing hints or
    ending the chance to guess the current word. This accepts "num_guess",
    "word_placeholder", "word_to_guess", and "game_area" as arguments.
    """
    def feedback_msg():
        """
        Checks if user input contains only letters, or is blank;
        and returns a feedback message.
        """
        if user_guess.isalpha() or user_guess == '':
            if user_guess != "":
                message = f"You answered '{user_guess}' which is incorrect. "
            else:
                message = ''
        else:
            message = "Only letters are allowed. "
        return message

    if guess_num == 1:
        utility.clear_terminal()
        placeholder = give_1st_hint(word, placeholder)
        print(game_zone)
        display_placeholder(placeholder)
        feedback_msg = feedback_msg()
        print(Fore.MAGENTA + f"{feedback_msg}CLUES ARE ADDED ABOVE.".center(80))
        print(utility.blank_lines(1))
        print("[For hint, press 'Enter']".center(80))
    elif guess_num == 2:
        utility.clear_terminal()
        placeholder = give_2nd_hint(word, placeholder)
        print(game_zone)
        display_placeholder(placeholder)
        feedback_msg = feedback_msg()
        print(Fore.MAGENTA + f"{feedback_msg}MORE CLUES ARE ADDED ABOVE.".center(80))
        print(utility.blank_lines(1))
        print("[To reveal the word, press 'Enter']".center(80))
    else:
        utility.clear_terminal()
        print(game_zone)
        display_placeholder(word)
        print(Fore.RED + "Sorry, you did not guess it!\n".center(80))


def check_user_guess(word, definition, placeholder, mode, game_zone):
    """
    Checks if the user's guess is correct or not and provides feedback.
    Allows the user to have 3 attempts only for each word.
    """
    not_guessed_yet = True
    tries_per_word = 0
    print("[For hint, press 'Enter']".center(80))

    while not_guessed_yet and tries_per_word != 3:
        guess = input(Fore.YELLOW + "Provide your guess (type the word):\n".center(80) + Style.RESET_ALL).upper()
        tries_per_word += 1
        if guess == word:
            utility.clear_terminal()
            not_guessed_yet = False
            Scorer.add_to_correct_guesses()
            points = Scorer.earn_points(tries_per_word)
            game_area = display_game_area(definition, mode)
            print(game_area)
            display_placeholder(word)
            print(Fore.YELLOW + "Correct!\n".center(80))
            if mode == 3:
                print(f"You earned: {points}"
                      f" point{'s' if points > 1 else ''}\n".center(80))
        else:
            feedback_to_wrong_guess(tries_per_word, placeholder, word,
                                    game_zone, guess)


def check_if_gameover(game_zone, word: str, max_num: int):
    """
    Checks if the game has reached the maximum words to end the game, and
    requires the arguments: "game area object" (game_zone), the "word to
    guess" (word) and the "maximum number of words before game over" (max_num).
    Returns True or False
    """
    def wrong_input_feedback(proceed_input, msg):
        """
        Provides feedback to user if input is invalid
        """
        while proceed_input != "y":
            utility.clear_terminal()
            print(game_zone)
            display_placeholder(word)
            print(Fore.RED + "Wrong input. Please enter 'Y' only.".center(80))
            print(utility.blank_lines(1))
            proceed_input = input(Fore.YELLOW + msg.center(80) + Style.RESET_ALL).lower()

    # Game ends after 15 words
    game_continues = True
    if len(Word.used_words) == max_num:
        game_continues = False
        prompt_msg = "Enter 'Y' to see your performance: \n"
        proceed = input(Fore.YELLOW + prompt_msg.center(80) + Style.RESET_ALL).lower()
        wrong_input_feedback(proceed, prompt_msg)
    else:
        prompt_msg = "Enter 'Y' to proceed to the next word:\n"
        proceed = input(Fore.YELLOW + prompt_msg.center(80) + Style.RESET_ALL).lower()
        wrong_input_feedback(proceed, prompt_msg)

        game_continues = True
    return game_continues


def play_game(game_mode):
    """
    Runs the game with specific game mode
    """
    game_on = True
    max_words = 15

    while game_on:
        utility.clear_terminal()

        game_object = game_mode_assembler(game_mode)
        game_area = game_object["game_area"]
        word_to_guess = game_object["word_obj"].word.upper()
        word_definition = game_object["word_obj"].definition
        word_placeholder = game_object["word_obj"].placeholder

        print(game_area)
        display_placeholder(word_placeholder)

        check_user_guess(word_to_guess, word_definition, word_placeholder,
                         game_mode, game_area)
        game_on = check_if_gameover(game_area, word_to_guess, max_words)


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
