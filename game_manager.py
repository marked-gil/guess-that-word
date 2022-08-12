"""
Docstring here
"""
import random
from colorama import init, Fore, Style
from word_manager import Word
from dictionary import easy_words, hard_words
from score_manager import Scorer
from arts import MINOR_LOGO
from utility_manager import UtilityTools as utility


# keeps color change within the text inside print statement
init(autoreset=True)


class Game():
    """
    Docstring here
    """
    max_words = 15

    def __init__(self, mode):
        self.game_mode = mode

    @staticmethod
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

    @staticmethod
    def display_placeholder(placeholder):
        """
        Displays the placeholder of the word
        """
        word_placeholder = '  '.join(placeholder).center(80)\
            + utility.blank_lines(3, "after_line")

        print(Fore.CYAN + word_placeholder)

    def game_mode_assembler(self):
        """
        Returns the "word object", and "game area" while accepting
        the "game mode" (mode) as argument.
        """
        if self.game_mode == 1:
            random_word = Word(easy_words)
        elif self.game_mode == 2:
            random_word = Word(easy_words)
        elif self.game_mode == 3:
            random_word = Word(easy_words) if len(Word.used_words) < 8 \
                else Word(hard_words)

        if self.game_mode in (1, 2):
            return {"word_obj": random_word, "game_area":
                    self.display_game_area(random_word.definition, self.game_mode)}

        return {"word_obj": random_word, "game_area":
                self.display_game_area(random_word.definition, self.game_mode)}

    @staticmethod
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

    @staticmethod
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

    def feedback_to_wrong_guess(self, guess_num, word_holder_dict, game_zone, user_guess):
        """
        Responds to every wrong guess by the user by providing hints or
        ending the chance to guess the current word. This accepts "num_guess",
        "word_placeholder", "word_to_guess", and "game_area" as arguments.
        """
        word = word_holder_dict["word"]
        placeholder = word_holder_dict["placeholder"]

        def feedback_msg():
            """
            Checks if user input contains only letters, or is blank;
            and returns the feedback message.
            """
            if user_guess.isalpha() or user_guess == '':
                if len(user_guess) > (len(word)):
                    message = "Your input is longer than the expected answer."
                elif user_guess != "":
                    message = f"You answered '{user_guess}' which is incorrect."
                else:
                    message = ''
            else:
                message = "Only letters are allowed. "
            return message

        if guess_num == 1:
            utility.clear_terminal()
            placeholder = self.give_1st_hint(word, placeholder)
            print(game_zone)
            self.display_placeholder(placeholder)
            feedback_msg = feedback_msg()
            if feedback_msg != '':
                print(Fore.RED + feedback_msg.center(80))
            print(Fore.MAGENTA + "CLUES ARE ADDED ABOVE.".center(80))
            print(utility.blank_lines(1))
            print("[For hint, press 'Enter']".center(80))
        elif guess_num == 2:
            utility.clear_terminal()
            placeholder = self.give_2nd_hint(word, placeholder)
            print(game_zone)
            self.display_placeholder(placeholder)
            feedback_msg = feedback_msg()
            if feedback_msg != '':
                print(Fore.RED + feedback_msg.center(80))
            print(Fore.MAGENTA + "MORE CLUES ARE ADDED ABOVE.".center(80))
            print(utility.blank_lines(1))
            print("[To reveal the word, press 'Enter']".center(80))
        else:
            utility.clear_terminal()
            print(game_zone)
            self.display_placeholder(word)
            print(Fore.RED + "Sorry, you did not guess it!\n".center(80))

    def check_user_guess(self, word, definition, placeholder, game_zone):
        """
        Checks if the user's guess is correct or not and provides feedback.
        Allows the user to have 3 attempts only for each word, and returns
        the updated game area.
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
                game_zone = self.display_game_area(definition, self.game_mode)
                print(game_zone)
                self.display_placeholder(word)
                print(Fore.YELLOW + "Correct!\n".center(80))
                if self.game_mode == 3:
                    print(f"You earned: {points}"
                        f" point{'s' if points > 1 else ''}\n".center(80))
            else:
                word_and_holder_dict = {"placeholder": placeholder, "word": word}
                self.feedback_to_wrong_guess(tries_per_word, word_and_holder_dict,
                                        game_zone, guess)
        return game_zone

    def check_if_gameover(self, game_zone, word: str, max_num: int):
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
                self.display_placeholder(word)
                print(Fore.RED + "Invalid input. Please enter 'Y' only.".center(80))
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

    def play_game(self):
        """
        Runs the game with specific game mode
        """
        game_on = True

        while game_on:
            utility.clear_terminal()

            game_object = self.game_mode_assembler()
            game_area = game_object["game_area"]
            word_to_guess = game_object["word_obj"].word.upper()
            word_definition = game_object["word_obj"].definition
            word_placeholder = game_object["word_obj"].placeholder

            print(game_area)
            self.display_placeholder(word_placeholder)

            game_area = self.check_user_guess(word_to_guess, word_definition, word_placeholder,
                                  game_area)
            game_on = self.check_if_gameover(game_area, word_to_guess, Game.max_words)

