"""
This module contains the Scorer class which tracks the user's
score and the number of correct guesses.
"""
from colorama import Fore
from localStoragePy import localStoragePy
from utility_manager import clear_terminal, blank_lines


class Scorer:
    """
    Tracks the user's score and number of correct guesses; and provides
    methods to locally store, retrieve, and reset the highscore; and to
    show user's performance.
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
        Determines the points earned, adds it to the total score.
        Returns: the points earned
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
        Retrieves the highscore from the local storage.
        Returns: saved highscore
        """
        local_storage = localStoragePy('guessthatword-hiscore')
        hi_score = local_storage.getItem("hi-score")
        return hi_score

    @staticmethod
    def store_highscore():
        """
        Stores the highscore in the localStorage.
        Returns: the local storage
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
    def show_performance(game_mode: int):
        """
        Displays the performance of the user.
        Parameter: game_mode
        Returns: score performance of user (in 'Beat the Highscore' mode)
        """
        clear_terminal()
        total_right_guesses = Scorer.total_correct_guesses
        print(blank_lines(6))
        print(Fore.MAGENTA + f"You correctly guessed {total_right_guesses} "
              f"word{'s' if total_right_guesses > 1 else ''} "
              "out of 15.\n".center(80))

        # Additional performance result in 'Beat the Highscore' mode
        if game_mode == 3:
            u_score = Scorer.total_score
            hi_score = Scorer.get_highscore()
            s_msg = ""
            if hi_score is None:
                s_msg = f"Your score is: {u_score}. (Saved as highscore.)\n"
                print(Fore.YELLOW + s_msg.center(80))
            elif int(hi_score) >= u_score:
                s_msg = f"Your score is: {u_score} || HIGHSCORE: {hi_score}\n"
                print(Fore.YELLOW + s_msg.center(80))
            elif int(hi_score) < u_score:
                s_msg = "Congratulations! You've just set the NEW HIGHSCORE: "\
                      + f"{u_score}\n"
                print(Fore.YELLOW + s_msg.center(80))
            return s_msg

    @staticmethod
    def validate_to_reset_highscore(score_msg):
        """
        Prompts user to reset highscore if desired, and validates
        the input.
        """
        local_storage = localStoragePy('guessthatword-hiscore')
        total_right_guesses = Scorer.total_correct_guesses

        print(blank_lines(3))
        while True:
            clear_hi_score = input("Do you want to reset the highscore? "
                                   "['Y' | 'N']:\n".center(80)).lower()
            # resets highscore
            if clear_hi_score == 'y':
                local_storage.removeItem("hi-score")
                clear_terminal()
                print(
                    blank_lines(6) +
                    "++++++++++++++++++++".center(80) +
                    "Highscore reset!".center(80) +
                    "++++++++++++++++++++".center(80) +
                    blank_lines(2, "after_line")
                    )
                break
            # does not reset highscore
            if clear_hi_score == 'n':
                clear_terminal()
                print(blank_lines(8))
                break

            # feedback to invalid input
            clear_terminal()
            print(blank_lines(6))
            print(Fore.MAGENTA + f"You correctly guessed {total_right_guesses}"
                  f" word{'s' if total_right_guesses > 1 else ''} "
                  "out of 15.\n".center(80))
            print(Fore.YELLOW + score_msg.center(80))

            print(
                blank_lines(3) +
                Fore.RED + "[Enter only 'Y' for Yes, or 'N' for No]".center(80)
                )
