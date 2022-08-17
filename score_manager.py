"""
This module contains the Scorer class which tracks the user's
score and number of correct guesses
"""
from colorama import Fore
from localStoragePy import localStoragePy
from utility_manager import clear_terminal, blank_lines


class Scorer:
    """
    Provides the user's total score, total number of correct guesses,
    and the created instance's current points earned
    """
    total_score = 0
    total_correct_guesses = 0

    @staticmethod
    def add_to_correct_guesses():
        """
        Adds each correct guess to the total number of correct guesses.
        """
        Scorer.total_correct_guesses += 1

    @staticmethod
    def earn_points(num_of_tries: int):
        """
        Determines the points earned, adds it to the total score
        and returns the points
        """
        if num_of_tries == 1:
            points = 5
        elif num_of_tries == 2:
            points = 3
        elif num_of_tries == 3:
            points = 1
        Scorer.total_score += points
        return points

    @staticmethod
    def get_highscore():
        """
        Gets highscore from the local storage and returns it
        """
        local_storage = localStoragePy('guessthatword-hiscore')
        hi_score = local_storage.getItem("hi-score")
        return hi_score

    @staticmethod
    def store_highscore():
        """
        Stores the highscore in the localStorage, and returns the local storage
        """
        u_score = Scorer.total_score
        local_storage = localStoragePy('guessthatword-hiscore')
        hi_score = local_storage.getItem("hi-score")

        if hi_score is None:
            local_storage.setItem("hi-score", u_score)
            hi_score = local_storage.getItem("hi-score")
        elif int(hi_score) < u_score:
            local_storage.setItem("hi-score", u_score)
        return local_storage

    @staticmethod
    def show_performance(mode: int):
        """
        Shows performance of the user.
        Parameter: game mode number
        """
        clear_terminal()
        total_right_guesses = Scorer.total_correct_guesses
        print(blank_lines(6))
        print(Fore.MAGENTA + f"You correctly guessed {total_right_guesses} "
              f"word{'s' if total_right_guesses > 1 else ''} "
              "out of 15.\n".center(80))
        if mode == 3:
            u_score = Scorer.total_score
            hi_score = Scorer.get_highscore()
            if hi_score is None:
                print(Fore.YELLOW + f"Your score is: {u_score}. (Saved as \
                      highscore.)\n".center(80))
            elif int(hi_score) > u_score:
                print(Fore.YELLOW + f"Your score is: {u_score} || HIGHSCORE is \
                      {hi_score}\n".center(80))
            elif int(hi_score) < u_score:
                print(Fore.YELLOW + f"Congratulations! You've just set the NEW \
                      HIGHSCORE: {hi_score}\n".center(80))

    @staticmethod
    def validate_to_reset_highscore(mode: int):
        """
        Prompts user to choose whether to reset highscore or not,
        and validates the input.
        """
        local_storage = localStoragePy('guessthatword-hiscore')

        print(blank_lines(3))
        while True:
            clear_hi_score = input("Do you want to reset the highscore? "
                                   "['Y' | 'N']:\n".center(80)).lower()
            if clear_hi_score == 'y':
                local_storage.removeItem("hi-score")
                clear_terminal()
                print(
                    blank_lines(6) +
                    "Highscore reset!".center(80) +
                    blank_lines(2, "after_line")
                    )
                break
            if clear_hi_score == 'n':
                clear_terminal()
                print(blank_lines(8))
                break

            clear_terminal()
            Scorer.show_performance(mode)
            print(
                blank_lines(3) +
                Fore.RED + "[Enter only 'Y' for Yes, or 'N' for No]".center(80)
                )
