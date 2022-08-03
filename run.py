import math
import os
from arts import LOGO
from dictionary import easy_words, hard_words
from word_manager import Word


def display_placeholder(placeholder, full_answer=False):
    """
    Displays the random word placeholder in the terminal, and
    accepts a boolean argument on whether the full answer is
    to be shown or not
    """
    if full_answer:
        print('   '.join(placeholder))
    else:
        print('  '.join(placeholder))


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
    Gives hint by adding the 2nd and middle letters of the word to
    the placeholder and returns the modified placeholder
    """
    second_letter = word[1]
    middle_letter = word[math.floor(len(word) / 2)]
    placeholder[1] = second_letter
    placeholder[math.floor(len(word) / 2)] = middle_letter
    return placeholder


def show_answer(word, placeholder):
    """
    Displays the correct answer by replacing the placeholder underscores
    with the correct letters and returns the modified placeholder
    """
    for ind, letter in enumerate(word):
        placeholder[ind] = letter
    return placeholder


def display_logo(logo):
    """
    Returns the game ascii logo
    """
    return f"{logo} \n {(' ' * 14)} Welcome to the game that will test your vocabulary.\n\n{'=' * 80}"


# Home <-- start
print(display_logo(LOGO))
wants_instruction = input("To read the instruction, press 'Y'; otherwise, press 'N' to continue.\n").lower()
# Home <-- end

# validates if user wants to read instruction <-- start
while wants_instruction not in ['y', 'n']:
    wants_instruction = input("Please press 'Y' to read the instruction; or, press 'N' to proceed to the game.\n").lower()
if wants_instruction == 'y':
    os.system('cls||clear')
    print(display_logo(LOGO))
    print(
        "HOW TO PLAY:\n"
        "1. There are 3 modes of the game you can choose to play:\n"
        "   a. Easy Mode - guess 15 EASY words\n"
        "   b. Hard Mode - guess 15 HARD words\n"
        "   c. Beat the Highscore - guess 15 EASY & HARD words with scoring\n"
        "2. You will be presented with a definition, and you need to guess the word that it defines\n"
        "3. You are allowed 3 attempts to guess the word.\n"
        "4. Before each attempt, you will be provided with clues:\n"
        "   a. 1st clue = the number of letters in the word\n"
        "   b. 2nd clue = the first and last letters\n"
        "   c. 3rd clue = additional 1 or 2 letters within the word\n"
    )
    proceed_to_menu = input("To proceed to the game, enter 'Y'; otherwise, enter 'N' to return home:\n")
elif wants_instruction == 'n':
    print("Proceed to the menu.")
    os.system('cls||clear')
# validates if user wants to read instruction <-- end

# Game Mode <-- start
print(
    "GAME MODES:\n"
    "  1. Easy Mode\n"
    "  2. Hard Mode\n"
    "  3. Beat the Highscore\n"
    )
game_mode_num = input("Choose a game mode by entering '1', '2', or '3'\n")
while game_mode_num not in ["1", "2", "3"]:
    game_mode_num = input("You need to enter '1', '2', or '3'\n")
if game_mode_num == "1":
    print(f"You chose Game Mode: {game_mode_num}")
elif game_mode_num == "2":
    print(f"You chose Game Mode: {game_mode_num}")
elif game_mode_num == "3":
    print(f"You chose Game Mode: {game_mode_num}")
# Game Mode <-- end

game_on = True

while game_on:
    selected_word = Word(easy_words)
    word_definition = selected_word.definition
    word_to_guess = selected_word.word.upper()

    print(f"Definition:\n\"{word_definition}\"")
    print("Used Words Id:", Word.used_words)

    word_placeholder = ["___" for _ in range(len(word_to_guess))]
    print('  '.join(word_placeholder))

    not_guessed_yet = True
    num_guess = 0

    while not_guessed_yet and num_guess != 3:
        guess = input("Provide your guess:\n").upper()

        if guess == word_to_guess:
            not_guessed_yet = False
            print("Correct!")
        else:
            num_guess += 1
            if num_guess == 1:
                word_placeholder = give_1st_hint(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder)
                print("Try again!")
            elif num_guess == 2:
                word_placeholder = give_2nd_hint(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder)
                print("Try again!")
            else:
                print("Sorry your guess is wrong!")
                answer = show_answer(word_to_guess, word_placeholder)
                display_placeholder(word_placeholder, True)

    # if len(used_words) == 10:
    #     print("GAME OVER!")
    #     game_on = False