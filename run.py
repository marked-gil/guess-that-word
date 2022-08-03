import math
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


# --> START
print(LOGO)
print("Welcome to the game that will test your vocabulary.")
wants_instruction = input("To read the instruction, press 'Y'; otherwise, press 'N' to continue.\n").lower()

# validates if user wants to read instruction <-- start
while wants_instruction not in ['y', 'n']:
    wants_instruction = input("Please press 'Y' to read the instruction; or, press 'N' to proceed to the game.\n").lower()
if wants_instruction == 'y':
    print("Here is the instruction.")
elif wants_instruction == 'n':
    print("Proceed to the menu.")
# validates if user wants to read instruction <-- end


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