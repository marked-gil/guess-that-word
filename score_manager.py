"""
This module contains the Scorer class which tracks the user's
score and number of correct guesses
"""


class Scorer():
    """
    Provides the user's total score, total number of correct guesses,
    and the created instance's current points earned
    """
    total_score = 0
    total_correct_guesses = 0

    def __init__(self, num_of_tries):
        self.points = self._get_points(num_of_tries)
        Scorer.total_score += self.points
        Scorer.total_correct_guesses += 1

    def _get_points(self, num_of_tries):
        if num_of_tries == 1:
            points = 5
        elif num_of_tries == 2:
            points = 3
        elif num_of_tries == 3:
            points = 1
        return points
