"""
This module contains the Scorer class which tracks the user's
score and number of correct guesses
"""
from colorama import Fore
from localStoragePy import localStoragePy
from utility_manager import UtilityTools

utility = UtilityTools()


class Scorer():
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
    def earn_points(num_of_tries):
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

    @staticmethod
    def validate_to_reset_highscore(storage_name):
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
