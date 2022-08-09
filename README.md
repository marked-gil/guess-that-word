# Guess That Word
<!-- use ezgif -->
**‘Guess that Word’** is a terminal game that tests the English vocabulary of its users by letting them guess words as they are defined. It gives them 3 game modes to choose from: (1) Easy, (2) hard, and (3) Beat the Highscore. The ‘Easy’ mode and ‘Hard’ mode each provide 15 words to guess and the number of correct guesses will be shown to the user at the end. For the ‘Beat the Highscore’ mode, the user will also be provided with 15 words (8 are easy, and 7 are hard) but with a scoring; and at the end of the game the total score will be shown and a highscore will be saved that the user can beat in the future. In all these modes of the game, 3 hints are provided: (1) the number of letters, (2) 1st and last letters - after first failed try, and (3) more letters within the word - after 2nd failed try.

## TABLE OF CONTENTS
<!-- table of contents here -->

___
## USER EXPERIENCE DESIGN (UXD)

### STRATEGY
#### Main Goal:
* The main goal of this game is to test the English vocabulary of its users, and/or help them learn English words while enjoying the excitement and stress-relieving nature of an online game. [View live website here.](https://guess-that-word-game.herokuapp.com/)

#### Target Audience:
1. People who want to test and challenge their English vocabulary.
2. People who enjoy learning the English language.
3. People who want to improve their English vocabulary and, at the same time, want to do it in a fun way.

#### User Stories:
1. As a user, I want to test my vocabulary by playing a game that provides a definition and I will have to guess the word it defines.
2. As a user, I want to learn new words to add to my vocabulary by playing a game.
3. As a user, I want to be able to choose an easy game mode that will provide easy words to guess.
4. As a user, I want to be able to choose a hard game mode that will provide hard words to guess.
5. As a user, I want the game to track my progress in building my vocabulary by scoring my correct guesses.
6. As a user, I want to challenge myself in the game by having the chance to beat my previous performance.
7. As a user, I want to have some help in guessing a word if I find it difficult by providing hints.
8. As a user,  I want to learn as I play by providing the correct answer immediately.

### SCOPE
#### Planned Features:
<!-- content here -->

#### Design Choice:
As this is a game played on a terminal, therefore the design option is limited, I still endeavoured to  make it as visually appealing, intuitive and simplistic as it can be. This is achieved by using ascii arts, making the terminal look uncluttered by clearing it after every group of displayed data/information, and providing only necessary data in the terminal at each moment.

### STRUCTURE
#### Interaction Choice:
<!-- content here -->

### SKELETON
<!-- Flow Diagram -->

### SURFACE
<!-- content here -->


## FEATURES
<!-- content here -->

## FIXED BUGS
<!-- content here -->

## BUGS LEFT TO FIX
<!-- content here -->

## TESTING
<!-- content here -->
<!-- Pep8 online -->

## DEPLOYMENT
<!-- content here -->

## TECHNOLOGIES USED
The following are the technologies used in this project:
* Programming Language:
    * Python
* Python Modules/Libraries:
    * [os](https://docs.python.org/3/library/os.html) - a built-in module to use operating-system-dependent functionality
    * [sys](https://docs.python.org/3/library/sys.html) - a built-in module where the sys.executable and sys.argv came from, which were passed into the os.execv method to restart the game.
    * [random](https://docs.python.org/3/library/random.html) - a built-in the module that generates pseudo-randomness.
    * [localStoragePy](https://pypi.org/project/localStoragePy/) - an external Python package that allows local storage of data
    * [colorama](https://pypi.org/project/colorama/) - an external Python package that colors the terminal text
* Gitpod — the cloud-based IDE (Integrated Developer Environment) used to build this site.
* Git — as a version control system, was used to monitor and record changes made when building the site. This allowed for the restoration of an earlier version of the code when it was necessary.
* GitHub — stores the source code repository for this website.
* Diffchecker - used when comparing codes tested in another IDE to the codes in gitpod.
* [Fsymbols](https://fsymbols.com/generators/carty/) - generates ascii text art
* For test and validating:
    * [pep8](http://pep8online.com/)

## CREDITS
<!-- content here -->

## ACKNOWLEDGMENT
<!-- content here -->