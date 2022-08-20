"""
This module contains the class Game which is responsible for
the main game's logical process.
"""
import random
from colorama import init, Fore, Style
from word_manager import Word
from dictionary import easy_words, hard_words
from score_manager import Scorer
from arts import MINOR_LOGO
from utility_manager import clear_terminal, blank_lines

# keeps color change within the text inside print statement
init(autoreset=True)


class Game:
    """
    Contains the logical process of the main game. This is
    run by calling its play_game() method.
    """
    max_words = 15

    def __init__(self, game_mode: int):
        self.game_mode = game_mode

    @staticmethod
    def _display_game_area(word_def: str, game_mode: int):
        """
        Returns the game area layout with modified content according to
        on the game mode selected by the user.
        Parameters: word_def (word definition), game_mode
        """
        if game_mode == 3:
            score_display = f"Score: {Scorer.total_score}"
            space = " " * 8
            mode = "BEAT THE HIGH SCORE"
            hi_score = Scorer.get_highscore()
            if hi_score is None:
                hi_score_display = "No Saved High Score"
            else:
                hi_score_display = f"High Score: {hi_score}"
        else:
            score_display = f"Correct Answers: {Scorer.total_correct_guesses}"
            space = " "
            if game_mode == 1:
                mode = "EASY MODE"
            elif game_mode == 2:
                mode = "HARD MODE"
            hi_score_display = ""

        total_words = len(Word.used_words)

        # game area layout
        game_area_template = f"\n  {Fore.GREEN + MINOR_LOGO} {space}\
        {score_display}       Words Left: {15 - total_words}\n"\
            + Style.RESET_ALL + "=" * 80\
            + "\n  " + mode\
            + hi_score_display.rjust(55)\
            + blank_lines(2, "inline")\
            + "Definition:".center(80)\
            + blank_lines(1, "inline")\
            + word_def.center(80)\
            + blank_lines(2, "after_line")\

        return game_area_template

    @staticmethod
    def _display_placeholder(placeholder):
        """
        Displays the placeholder of the word
        """
        word_placeholder = '  '.join(placeholder).center(80)\
            + blank_lines(3, "after_line")

        print(Fore.CYAN + word_placeholder)

    def _game_mode_assembler(self):
        """
        Assembles the game mode selected by the user by returning an
        instance of the class Word, and the modified game area layout.
        Returns: a dictionary of "word_obj" (a Word instance) and
        "game_area" (game area layout)
        """
        # Instantiates the Word class based on the game mode selected
        if self.game_mode == 1:
            word_instance = Word(easy_words)
        elif self.game_mode == 2:
            word_instance = Word(hard_words)
        elif self.game_mode == 3:
            word_instance = Word(easy_words) if len(Word.used_words) < 8 \
                else Word(hard_words)

        return {"word_obj": word_instance, "game_area":
                self._display_game_area(word_instance.definition,
                                        self.game_mode)}

    @staticmethod
    def _give_1st_hint(word, placeholder):
        """
        Gives hint by adding the first and last letters of the word to
        the placeholder.
        Returns: modified placeholder
        """
        first_letter = word[0]
        last_letter = word[-1]
        placeholder[0] = first_letter
        placeholder[-1] = last_letter

        return placeholder

    @staticmethod
    def _give_2nd_hint(word, placeholder):
        """
        Gives hint by adding more letters (between the first and
        last letters) to the placeholder.
        Returns: modified placeholder
        """
        indx_list = []
        num_characters = len(word)

        # adds 2 letters if word has < 8 characters
        if num_characters < 8:
            while len(indx_list) != 2:
                indx = random.randrange(1, num_characters-1)
                if indx not in indx_list:
                    indx_list.append(indx)
        # adds 3 letters if word has 8 or 9 characters
        elif num_characters <= 9:
            while len(indx_list) != 3:
                indx = random.randrange(1, num_characters-1)
                if indx not in indx_list:
                    indx_list.append(indx)
            placeholder[indx_list[2]] = word[indx_list[2]]
        # adds 4 letters if word has > 10 characters
        elif num_characters >= 10:
            while len(indx_list) != 4:
                indx = random.randrange(1, num_characters-1)
                if indx not in indx_list:
                    indx_list.append(indx)
            placeholder[indx_list[2]] = word[indx_list[2]]
            placeholder[indx_list[3]] = word[indx_list[3]]

        placeholder[indx_list[0]] = word[indx_list[0]]
        placeholder[indx_list[1]] = word[indx_list[1]]

        return placeholder

    def _feedback_to_wrong_guess(self, guess_num: int, word_holder_dict,
                                 game_zone, user_guess: str):
        """
        Responds to every wrong guess by either giving hints or ending the
        chance to guess the current word.
        Parameters: guess_num (number of tries), word_holder_dict (word &
        placeholder), game_zone (game area layout), user_guess
        """
        word = word_holder_dict["word"]
        placeholder = word_holder_dict["placeholder"]

        def feedback_msg():
            # Returns the feedback message
            if user_guess.isalpha() or user_guess == '':
                if len(user_guess) > (len(word)):
                    message = "Your input is longer than the expected answer"
                elif user_guess != "":
                    message = f"You answered '{user_guess}' which is incorrect"
                else:
                    message = ''
            else:
                message = "Only letters are allowed. "
            return message

        # after user's 1st failed try to guess the word
        if guess_num == 1:
            clear_terminal()
            placeholder = self._give_1st_hint(word, placeholder)
            print(game_zone)
            self._display_placeholder(placeholder)
            feedback_msg = feedback_msg()

            # displays feedback message
            if feedback_msg != '':
                print(Fore.RED + feedback_msg.center(80))
            print(Fore.MAGENTA + "CLUES ARE ADDED ABOVE.".center(80))
            print(blank_lines(1))
            print("[For hint, press 'Enter']".center(80))

        # after user's 2nd failed try to guess the word
        elif guess_num == 2:
            clear_terminal()
            placeholder = self._give_2nd_hint(word, placeholder)
            print(game_zone)
            self._display_placeholder(placeholder)
            feedback_msg = feedback_msg()

            # displays feedback message
            if feedback_msg != '':
                print(Fore.RED + feedback_msg.center(80))
            print(Fore.MAGENTA + "MORE CLUES ARE ADDED ABOVE.".center(80))
            print(blank_lines(1))
            print("[To reveal the word, press 'Enter']".center(80))

        # after user's 3rd failed try to guess the word
        else:
            clear_terminal()
            print(game_zone)
            self._display_placeholder(word)
            print(Fore.RED + "Sorry, you did not guess it!\n".center(80))

    def _check_user_guess(self, word: str, definition: str, placeholder,
                          game_zone):
        """
        Checks the user's guess, provides feedback, and displays the updated
        game area. It also allows the user to have only 3 attempts for each
        word.
        Parameters: word, definition, placeholder, game_zone (game area layout)
        Returns: updated game area layout
        """
        not_guessed_yet = True
        tries_per_word = 0
        print("[For hint, press 'Enter']".center(80))

        while not_guessed_yet and tries_per_word != 3:

            guess = input(Fore.YELLOW + "Provide your guess (type the word):\n"
                          .center(80) + Style.RESET_ALL).upper()
            tries_per_word += 1

            # word correctly guessed by user
            if guess == word:
                clear_terminal()
                not_guessed_yet = False
                Scorer.add_to_correct_guesses()
                points = Scorer.earn_points(tries_per_word)
                game_zone = self._display_game_area(definition, self.game_mode)
                print(game_zone)
                self._display_placeholder(word)
                print(Fore.YELLOW + "Correct!\n".center(80))

                # display points earned for game mode 3 (Beat the High Score)
                if self.game_mode == 3:
                    print(f"You earned: {points}"
                          f" point{'s' if points > 1 else ''}\n".center(80))

            # word not guessed by user
            else:
                word_and_holder = {"placeholder": placeholder, "word": word}
                self._feedback_to_wrong_guess(tries_per_word, word_and_holder,
                                              game_zone, guess)

        return game_zone

    def _check_if_gameover(self, game_zone, word: str, max_num: int):
        """
        Checks if game has reached the maximum number of words to end game.
        Parameters: game_zone (game area layout), word, max_num (max number
        of words to end game)
        Returns: True or False
        """
        def wrong_input_feedback(proceed_input, msg):
            # Displays feedback to user if input is invalid
            while proceed_input != "y":
                clear_terminal()
                print(game_zone)
                self._display_placeholder(word)
                print(blank_lines(1))
                print(Fore.RED + "Invalid input. Please enter Y only."
                      .center(80))
                proceed_input = input(Fore.YELLOW + msg.center(80) +
                                      Style.RESET_ALL).lower()

        game_continues = True

        # Game ends after 15 words
        if len(Word.used_words) == max_num:
            game_continues = False
            prompt_msg = "Enter Y to see your PERFORMANCE: \n"
            proceed = input(Fore.YELLOW + prompt_msg.center(80) +
                            Style.RESET_ALL).lower()
            wrong_input_feedback(proceed, prompt_msg)
        else:
            prompt_msg = "Enter Y to proceed to the next word:\n"
            proceed = input(Fore.YELLOW + prompt_msg.center(80) +
                            Style.RESET_ALL).lower()
            wrong_input_feedback(proceed, prompt_msg)

            game_continues = True

        return game_continues

    def play_game(self):
        """
        Runs the game and its logic
        """
        game_on = True

        while game_on:
            clear_terminal()

            # assembles the word challenge
            game_object = self._game_mode_assembler()
            game_area = game_object["game_area"]
            word_to_guess = game_object["word_obj"].word.upper()
            word_definition = game_object["word_obj"].definition
            word_placeholder = game_object["word_obj"].placeholder

            # displays the game area
            print(game_area)
            self._display_placeholder(word_placeholder)

            # checks the user's guess and the continuation of the game
            game_area = self._check_user_guess(word_to_guess, word_definition,
                                               word_placeholder, game_area)
            game_on = self._check_if_gameover(game_area, word_to_guess,
                                              Game.max_words)
