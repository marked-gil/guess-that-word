"""
This module contains utility functions
"""
import os
import sys


class UtilityTools():
    """
    Docstring here
    """
    @staticmethod
    def clear_terminal():
        """
        Clears the terminal
        """
        print("\033c")

    @staticmethod
    def blank_lines(num_lines, line_type="print_line"):
        """
        Adds specific number of blank lines for styling purposes & has
        2 parameters: "number of blank lines" and "line type".
        "line_type" accepts "print_line", "inline", and after_line"
        as arguments. "print_line" (default) if the function is directly placed
        inside print(); "inline" if function is concatenated in a string but
        not at the end; and "after_line" if function is concatenated at end
        of a string. This function eturns the number of blank lines to be
        printed in the terminal.
        """
        if line_type == "print_line":
            num_lines -= 1
        elif line_type == "inline":
            num_lines += 1
        elif line_type == "after_line":
            num_lines += 0

        return "\n" * num_lines

    @staticmethod
    def return_home():
        """
        Refreshes the game and goes back to home
        """
        os.execv(sys.executable, ['python'] + sys.argv)
