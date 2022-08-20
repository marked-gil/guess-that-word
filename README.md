# Guess That Word
![sample_clip](docs/screeshots/intro_shot.gif)     
**Guess that Word** is a terminal game that tests the English vocabulary of its users by letting them guess words as they are defined. It gives them 3 game modes to choose from: (1) Easy, (2) Hard, and (3) Beat the High Score. The ‘Easy’ mode and ‘Hard’ mode each provide 15 words to guess and the number of correct guesses will be shown to the user at the end. For the ‘Beat the High Score’ mode, the user will also be provided with 15 words (8 are easy, and 7 are hard) but with a scoring; and at the end of the game the total score will be shown and a high score will be saved locally which the user can beat in the future. In all these modes of the game, 3 hints are provided: (1) the number of letters through the placeholder (underscores), (2) the 1st and last letters (after the first failed guess), and (3) additional revealed letters (after 2nd wrong guess). For each word, the user is only allowed to guess three (3) times. [View live website.](https://guess-that-word-game.herokuapp.com)

## TABLE OF CONTENTS
* [User Experience Design (UXD)](#user-experience-design-uxd)
    * [Strategy](#strategy)
        * [Main Goal](#main-goal)
        * [Target Audience](#target-audience)
        * [User Stories](#user-stories)
    * [Scope](#scope)
        * [Planned Features](#planned-features)
        * [Design Choice](#design-choice)
    * [Structure](#structure)
    	* [Interaction Design](#interaction-design)
    * [Skeleton](#skeleton)
        * [Data Model](#data-model)
    * [Surface](#surface)
* [Features](#features)
    * [Home](#home)
    * [How To Play](#how-to-play)
    * [Game Modes](#game-modes)
    * [Game Area](#game-area)
    * [Hints](#hints)
    * [Display of Correct Answer](#display-of-correct-answer)
    * [Input Prompts](#input-prompts)
    * [Input Validations and Feedbacks](#input-validations-and-feedbacks)
    * [Input Case-Insensitivity](#input-case-insensitivity)
    * [Scoring System](#scoring-system)
    * [Saving of Highscore](#saving-of-highscore)
    * [Performance Display](#performance-display)
    * [Resetting the Highscore](#resetting-the-highscore)
    * [Re-running the Program](#re-running-the-program)
    * [No-scrolling Screen](#no-scrolling-screen)
* [Fixed Bugs](#fixed-bugs)
* [Bugs Left To Fix](#bugs-left-to-fix)
* [Testing](#testing)
	* [Test Cases](#test-cases)
    * [Pep8 Checker](#pep8-online-checker)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)
* [Acknowledgment](#acknowledgment)

___
## USER EXPERIENCE DESIGN (UXD)

### STRATEGY
#### Main Goal:
* The main goal of this game is to test the English vocabulary of its users, and/or help them learn English words while enjoying the excitement and stress-relieving nature of an online game. [View live website here.](https://guess-that-word-game.herokuapp.com/)

#### Target Audience:
* People who want to test and challenge their English vocabulary.
* People who enjoy learning the English language.
* People who want to improve their English vocabulary and, at the same time, want to do it in a fun way.

#### User Stories:
* As a user, I want to test my English vocabulary by playing a game that provides a definition and I will have to guess the word it defines.
* As a user, I want to learn new words to add to my vocabulary by playing a game.
* As a user, I want to have some help in guessing a word if I find it difficult by providing hints.
* As a user, I want to be able to choose an easy game mode that will provide easy words to guess.
* As a user, I want to be able to choose a hard game mode that will provide hard words to guess.
* As a user, I want the game to track my progress in building my vocabulary by scoring my correct guesses.
* As a user, I want to challenge myself in the game by having the chance to beat my previous performance.
* As a user, I want the high score to be saved and be reset if desired.
* As a user,  I want to learn as I play by providing the correct answer immediately.

[Back to Table of Contents](#table-of-contents)

### SCOPE
#### **Planned Features:**
Using the user stories, I have planned the following features:
* User Story:
    > As a user, I want to test my English vocabulary by playing a game that provides a definition and I will have to guess the word it defines.
    * IMPLEMENTATION:
        * The game will show a word definition to the user and they will be asked to guess the word it defines by typing it in the terminal.
* User Story:
    > As a user, I want to learn new words to add to my vocabulary by playing a game.  
    * IMPLEMENTATION:
        * The game will show the correct answer after every word challenge.
* User Story:
    > As a user, I want to have some help in guessing a word if I find it difficult by providing hints.
    * IMPLEMENTATION:
        * Three (3) hints will be provided in every word challenge. The initial hint will be the number of characters by showing a placeholder (underscore) for each letter in the word. If the user is unable to guess on the 1st try, the 2nd hint will reveal the first and last letters. If the user still cannot guess it, the 3rd hint will reveal additional letters of the word.
* User Story:
    > As a user, I want to be able to choose an easy game mode that will provide basic words to guess.
    * IMPLEMENTATION:
        * The game will include an easy mode which will provide common and mostly short words that the user will guess.
* User Story:
    > As a user, I want to be able to choose a hard game mode that will provide hard words to guess.
    * IMPLEMENTATION:
        * The game will include a hard mode which will provide either long words or words that are relatively not common.
* User Story:
    > As a user, I want the game to track my progress in building my vocabulary by scoring my correct guesses.
    * IMPLEMENTATION:
        * The game will include a 'Beat the High Score' mode, which will have a scoring system. In each word challenge, if the user correctly guesses the word on the 1st try, they will earn 5 points; if on the 2nd try, they will have 3 points, and on the 3rd try, 1 point will be awarded.
* User Story:
    > As a user, I want to challenge myself in the game by having the chance to beat my previous performance.
    * IMPLEMENTATION:
        * In the 'Beat the High Score' mode, the total score of the user will be displayed at the end of the game and will be compared to the high score saved on their computer. If the user's score is the first score or highest score played on their computer, it will be saved locally to set as, or to replace, the high score.
* User Story:
    > As a user, I want the high score to be saved, and reset if desired.
    * IMPLEMENTATION:
        * The high score will be saved locally on the user's computer, and the user will be given the option to reset it at the end of the game in the 'Beat the High Score' mode.
* User Story:
    > As a user,  I want to learn as I play by providing the correct answer immediately.
    * IMPLEMENTATION:
        * After each word challenge, the correct word will be displayed along with its definition before proceeding to the next word to guess.

#### **Design Choice:**
As this is a game played on a terminal, therefore the design option is limited, I still endeavoured to make it as visually appealing, intuitive and simplistic as it can be. This is achieved by using ASCII arts, making the terminal look uncluttered by clearing it after every group of displayed data/information, and providing only necessary data in the terminal at each moment.

[Back to Table of Contents](#table-of-contents)

### STRUCTURE
#### **Interaction Design**
* Clear & Intuitive Feedback
    * All invalid inputs to the prompts are handled with appropriate and clear feedback messages that usually hint to the user on how to correct them. In any case that the feedback message does not inform the user of what to do to have a valid input, the original prompt is displayed for the user to read again.
    * In the word challenge, if the user enters a wrong answer (including a single letter, but not longer than the correct word) their input will be displayed, and they will be asked to try again; if they enter a word or group of letters longer than the correct word, the feedback will specify this issue; and if they enter a character that is not in the English alphabet, the feedback message will also specify this.
* Consistent
    * Consistency is seen in various features of the program.
    * How the feedback messages are displayed is consistent. Its colour is always red and rests on top of the original prompt. And all displayed data/information are centre-aligned.
* Predictable
    * Predictability is evident in this program. When an input is entered, the user can predict that a feedback message will show if the input is invalid; and if it is valid, the program will continue.
    * On the game area, the definitions, placeholders, prompts and feedback are almost always expected to be displayed in the same spots due to the single-screen and no-scrolling feature of the program. This helps the user to locate these data easily and avoids confusion and enhances the user-friendly interface of the program.
    * The program always does what its prompt tells the user that it will do if a valid input is entered.
* Learnability
    * The user is provided with specific, easy-to-understand, and succinct prompts as the user runs the program. This enhances the learnability of the program and the game itself.
    * The game is also designed to be simple and intuitive, and, thus, learnable.
    * Due to its clean, uncluttered and simplified layout, the user can easily see all the data/information on the terminal screen.
* Functional Minimalism
    * The program prevents overwhelming the user with displayed data on the screen by keeping the program clean, simple, uncluttered, and minimalist. Only appropriate and needed groups of information are provided at each time. This is made possible by the clear_terminal function that this program utilizes, which keeps the terminal screen from being a long scrollable screen.
    * As this is a terminal game, the user can only provide input when it is prompted.

[Back to Table of Contents](#table-of-contents)

### SKELETON
#### **Data Model**
* **Program Flowchart**     
Below is the flowchart of the main process of this Python program. It starts with the Home section, which displays the main LOGO, and ends with the prompt for the user to play again. It shows the entire cycle of the program.
![Program Flowchart](docs/charts/program-flowchart.png)

* **Functions, Classes, & Imports Relational Diagram**  
The following diagram shows the flow of the functions inside the main() function, which holds the entire process of the program - from start to finish and back. It also reveals the relationship of the functions, classes and imported modules with each other.   
The **solid arrow lines** imply the sequential flow of the functions, while the **broken arrow lines** symbolize the direct relationship of the classes, modules, and libraries (internal & external) to each other.
![Relational Diagram](docs/charts/relational-diagram.png)

[Back to Table of Contents](#table-of-contents)

### SURFACE
* **Ascii arts**    
The following ASCII arts are taken from [fsymbols](https://fsymbols.com/generators/carty/). The first one is used as the main welcome logo, and the second one is displayed on the heading of the game area.       
![ascii logo 1](docs/screeshots/ascii-logo-1.png)
![ascii logo 2](docs/screeshots/ascii-logo-2.png)

* **Colorama**  
The [Colorama](https://pypi.org/project/colorama/) library is used to provide colour to the terminal texts. Aside from its aesthetic purpose, it also enhances the meaning and importance of the displayed message or information.

* To see features of the final product, go to [FEATURES](#features).

[Back to Table of Contents](#table-of-contents)

## FEATURES
### **Home**    
* The 'Home' section is the first display of texts/data in the terminal when the program runs. It contains the ASCII art logo/title with a line of text underneath it. Also, it shows a prompt for the user to enter an input either 'Y' to see the instruction on how to play or 'N' to proceed to the Game Menu.
![Home screenshot](docs/screeshots/home.png)

### **How to Play** 
* As the user enters the designated input (enter 'Y') to view the instruction while in the 'Home' section, the 'How to Play' content will be revealed below the ASCII art logo inside the 'Home' section.
![How to Play screenshot](docs/screeshots/how-to-play.png)

### **Game Modes**
* The different game modes will be shown under the ASCII art logo/title, and the user will be prompted to choose among the options by entering either number '1', '2', or '3'.
* There are 3 game modes that the user can play: [1] Easy mode, [2] Hard mode, and [3] Beat the High Score. Each of these modes will provide 15 words for the user to guess. The **Easy mode** will give easy or common words, and are usually short, while the **Hard mode** will give relatively difficult or uncommon words, and can sometimes be long. And the **Beat the High Score** mode will be a combination of easy & hard words (the first 8 words are easy, and the rest are hard) with the added feature of a scoring system and high score challenge.
[See 'How to Play' section.](#how-to-play)
![Game modes screenshot](docs/screeshots/game-modes.png)    

### **Game Area**
* The game area is where the game happens. It has a header which contains the game title (to the left) and the number of words left to guess. The 'Easy' and 'Hard' modes have an added display of correct guesses, while the 'Beat the Higshcore' mode has the score tracker display.
* It also displays the definition of the word to guess and the word placeholders, which are underscores equivalent to the number of letters the word has.
* Inside the game area, the user will be prompted to provide their guess. The answer (input) has to be the full word and correctly spelt. The input is not case-sensitive, so both upper and lower cases are accepted.
    * **'Easy Mode' game area**     
    ![Easy Mode game area](docs/screeshots/game-area-1.png)
    * **'Hard Mode' game area**     
    ![Hard Mode game area](docs/screeshots/game-area-2.png)
    * **'Beat the High Score' game area**        
    ![Beat the High Score game area](docs/screeshots/game-area-3.png)

### **Hints**
To make the game more fun and less arduous, hints to the answer are provided. For every word challenge, there are 3 hints provided:   
* 1st hint - the "number of characters" the word has through the placeholders (underscores) that are displayed on the game area.    
* 2nd hint - 1st and last letters of the word.
* 3rd hint - more supplied letters: 2 more letters if the word has less than 8 characters; 3 letters if the word has 8 or 9 characters; and 4 letters if the word has at least 10 characters.
![Hints screenshot](docs/screeshots/hints.png)

### **Display of Correct Answer**
The correct answer is revealed immediately after 3 wrong guesses.
![Display of correct answer](docs/screeshots/correct-answer.png)

### **Input prompts**
As this is a Python terminal game, the user is required to use their keyboard to type in an input to the program. Prompts are provided, which are yellow-coloured texts, and will specify the required input to proceed in the game.    
![Input prompt 1](docs/screeshots/prompt-1.png)     
![Input prompt 2](docs/screeshots/prompt-2.png)     

### **Input Validations and Feedbacks**
All inputs that the user will enter into the program as prompted will be validated to check if it follows the specified and required data input. If the user's input fails the validation, the game will return a feedback message which will be a red-coloured text to inform that user that they have entered an invalid input. These feedback messages will show at the top of the input prompt.       
* Sample 1:
    * ![Input feedback 1](docs/screeshots/input-feedback-1.png)   
* Sample 2:
    * ![Input feedback 2](docs/screeshots/input-feedback-2.png)

### **Input Case-Insensitivity**
Upper case or lower case or a combination of both are allowed as input.     
* ![case-insensitive input](docs/screeshots/case-insensitive.png)     

### **Scoring System**
The 'Beat the High Score' game mode has a scoring system in place. For each word challenge, when the user correctly guesses the word on the first try, they earn 5 points; on the 2nd try (with 2nd hint), 3 points are awarded; and on the 3rd try (with 3rd hint), 1 point is added to their total score. A score tracker is displayed at the header of the game area.  
![scoring system](docs/screeshots/scoring.png)

### **Saving of High Score**
* On the 'Beat the High Score' mode, the high score in the game will be saved locally. This high score will be compared with the current player's score at the end of the game and will be shown as text feedback.
* If the current user's score is higher than the last recorded high score, it will be replaced with the user's current score as the new high score. Text feedback confirming this will also be shown on the terminal.
* If there is no recorded high score, the current user's score will be recorded as the high score.   
![High Score local saving](docs/screeshots/hi-score-saving.png)

### **Performance Display**
When the user finishes the 15-word challenge, a prompt will ask the user to see their performance result by entering a specified key. When the required input is entered, the following will be displayed:
* For 'Easy' and 'Hard' game modes, their total number of correct guesses will be revealed.
* For the 'Beat the High Score' game mode, the program will show the total number of correct guesses, and their total score.       
![Performance display](docs/screeshots/performance_display.png)

### **Resetting the High Score**
On the 'Beat the High Score' mode, the user is given the control to choose to reset the high score at the end of the game.
![Reset high score](docs/screeshots/reset-highscore.png)

### **Re-running the Program**
As the user finishes the game, they are asked if they want to play again. And if they wish to re-run the game to play, they will need to enter the letter 'Y' to proceed.       
![Re-running the program](docs/screeshots/rerunning-program.png)

### **No-scrolling Screen**
This program prevents scrolling of a long screen page by displaying only a group of data that can fit the screen at each moment. It does not allow for texts to be repeatedly printed on the screen, which could make it look untidy and overwhelming to the user. This feature creates a more user-friendly and intuitive interface.

[Back to Table of Contents](#table-of-contents)

## FIXED BUGS
* **ISSUE:**  
When I ran the program after refactoring the script into different modules, an error showed up which states `ImportError: cannot import name 'Game' from partially initialized module 'game_manager' (most likely due to a circular import)`.  

    * **INTENDED OUTCOME:**    
    I expect the script to still run as smoothly as it had without any error before I refactored the code.    

    * **SOLUTION:**     
    After some research on the web, [bobbyhadz blog](https://bobbyhadz.com/blog/python-importerror-cannot-import-name) gave me the idea to solve the problem.
    I realized that the problem occurred because I imported the score_manager module into the game_manager module, and vice versa. This resulted in the ImportError due to a circular import. So to solve this, I removed the accidentally imported game_manager module from the score_manager module, and the program ran perfectly.   

* **ISSUE:**       
I noticed that when I played the 'Beat the High Score' game mode, the score tracker being displayed at the top of the terminal screen would revert the score to the previous result when a wrong input is entered to proceed to the next word challenge. 

    * **INTENDED OUTCOME:**     
    I expect the score tracker to display the score consistently without fail. The added points should be reflected in the score as soon as the player correctly guessed the word, and it should not change until another point is added to it.   

    * **SOLUTION:**     
    As this was a logical error, I traced back the code, especially the validator for wrong inputs on that certain section. After some deep thoughts and analysis, I found the cause, updated the passed-in argument to the involved function, and it finally worked perfectly as intended.

[Back to Table of Contents](#table-of-contents)

## BUGS LEFT TO FIX
After thorough manual testing of the site, there were no bugs that I found.

## TESTING
### **Test Cases**
![Test cases 1](docs/test-cases/test-cases-1.png)
![Test cases 2](docs/test-cases//test-cases-2.png)
![Test cases 3](docs/test-cases//test-cases-3.png)
![Test cases 4](docs/test-cases//test-cases-4.png)
![Test cases 5](docs/test-cases//test-cases-5.png)
![Test cases 6](docs/test-cases//test-cases-6.png)
![Test cases 7](docs/test-cases//test-cases-7.png)
![Test cases 8](docs/test-cases//test-cases-8.png)

[Back to Table of Contents](#table-of-contents)

### **Pep8 Online Checker**
Using the [Pep8 Online Checker](http://pep8online.com/), the Python code in this site is compliant to the Pep8 requirements.
* run.py module     
![run module pep 8 result](docs/pep8-results/pep8-check-run.png)
* game_manager module       
![game_manager module pep8 result](docs/pep8-results/pep8-check-game.png)   
* score_manager module
![score_manager module pep8 result](docs/pep8-results/pep8-check-scorer.png)    
* word_manager module       
![word_manager module pep8 result](docs/pep8-results/pep8-check-word.png)
* utility_manager module      
![utility_manager module pep8 result](docs/pep8-results/pep8-check-utility.png)    
* dictionary.py
![dictionary module pep8 result](docs/pep8-results/pep8-check-dictionary.png)
* arts.py       
![arts pep8 result](docs/pep8-results/pep8-check-arts.png)

[Back to Table of Contents](#table-of-contents)

## DEPLOYMENT

### **Version Control**
**Git** was a crucial tool used to track changes that were made in the repository. The following git commands were mainly used in developing this program:

* `git status` — to show the status of the repository by displaying the files that have been staged and are ready for commit, those that are not, and those that are untracked.
* `git add <file name>` — to add file or changes in the file to the staging area before they can be committed
* `git commit -m "message"` — to add/record files or changes to the local repository
* `git push` — to upload the local repository to the remote repository, such as GitHub

### **Heroku Deployment**
This website is published on [Heroku](https://www.heroku.com). The following were the steps I took for this project's deployment.
1. I logged in to my Heroku account.
2. Then, I was redirected to this URL `https://dashboard.heroku.com/apps`. Inside, I clicked the 'New' button which was a dropdown menu. Between the two (2) options it showed, I clicked on 'Create new app'.
3. Then, on the 'Create New App' page, I typed in my 'app name' and 'region' on their respected input fields. Then I clicked the 'create app' button that is sitting at the bottom of the aforementioned fields. This then redirected me to my new app's page in Heroku.
4. On my new app's page, there is a row of links, which includes: Overview, Resources, Deploy, Metrics, Activity, Access, and Settings. 
5. I first went to 'Settings' by clicking its link. Inside the 'Settings', I clicked on 'Reveal Config Vars' and added 'PORT' in the key field, and '8000' in the value field, then clicked on the 'add' button beside them.
6. Then, on the 'Buildpacks' section, I clicked the 'Add buildpack' button and added python (1st) and nodejs (2nd) - the ordering is important.
7. Then, I went to the 'Deploy' link and clicked on Github as the Deployment Method.
8. Below the Deployment Method section is the Connect to Github section. Here I searched for the name of my new app on Github using the search input field provided. When the name of the repository was displayed, I clicked on the 'connect' button.
9. After a few minutes, it revealed a button to view the deployed website.

### **Cloning from Github**
To clone the repository for this site, do the following steps:  
1. Go to this URL: https://github.com/marked-gil/guess-that-word
2. Inside the repository, look for the button labelled as '**Code**', which is along the rows with other buttons such as 'Go to file' and 'Add file'.
3. Click on the '**Code**' button, and a small popup box will show up with a top heading of '**Clone**'.
4. In the popup box, click on the 'HTTPS' link and copy the URL just below it.
5. Then, go to your computer's terminal and type `git clone https://github.com/marked-gil/guess-that-word`
6. A copy of the repository is now saved on your computer.

[Back to Table of Contents](#table-of-contents)

## TECHNOLOGIES USED
The following are the technologies used in this project:
* Programming Language:
    * Python
* Python Modules/Libraries:
    * [os](https://docs.python.org/3/library/os.html) - a built-in module to use operating-system-dependent functionality. This is used in the program, along the with `sys` module, to refresh/re-start the program.
    * [sys](https://docs.python.org/3/library/sys.html) - a built-in module where the sys.executable and sys.argv came from, which were passed into the os.execv method to restart the game.
    * [random](https://docs.python.org/3/library/random.html) - a built-in module that generates pseudo-randomness. This was used in adding randomness to the selection of words from the custom dictionary module, and to the randomness of the provision of letters as hints.
    * [localStoragePy](https://pypi.org/project/localStoragePy/) - an external Python package that allows local storage of data. This is used to locally store the high score in the Beat the High Score mode.
    * [colorama](https://pypi.org/project/colorama/) - an external Python package that colors the terminal text. This adds to the aesthetic appeal of the game.
* Gitpod — the cloud-based IDE (Integrated Developer Environment) used to build this site.
* Git — as a version control system, was used to monitor and record changes made when building the site. This allowed for the restoration of an earlier version of the code when it was necessary.
* GitHub — stores the source code repository for this website.
* [LucidCharts](https://www.lucidchart.com/) - used in creating the flowcharts/diagram for the data model.
* [Diffchecker](https://www.diffchecker.com/) - used when comparing codes tested in another IDE to the codes in gitpod.
* [Fsymbols](https://fsymbols.com/generators/carty/) - generates ascii text art
* [pep8](http://pep8online.com/) - used to check the Python script for compliance with PEP8 requirements
* [TinyPng](https://tinypng.com/) - used to compress the images displayed in the README file.
* [Ezgif](https://ezgif.com/) - used to create the snippet of this program's functionality by converting the video into a gif.
* [Grammarly](https://www.grammarly.com) - used to check the grammar of the contents in this project.


[Back to Table of Contents](#table-of-contents)

## CREDITS
### **Content**
* Words & Definitions   
The words and definitions used in this game are taken from [Merriam-Webster](https://www.merriam-webster.com/).

* Ascii Arts 
    * [fsymbols](https://fsymbols.com/generators/carty/) - where all the ASCII arts used in this site are taken from.

### **References**
* Main Python references:
    * [Code Institute Lessons](https://codeinstitute.net/ie/)
    * [W3Schools](https://www.w3schools.com/)
    * [Geeks for Geeks](https://www.geeksforgeeks.org/)
    * [Python.org](https://docs.python.org/3/)      

* [Tech with Tim Youtube video](https://www.youtube.com/watch?v=MpuOuZKWUWw) - for static vs class methods      

* [Stackoverflow](https://stackoverflow.com/), especially for the following links:      
    * [A simple method to clear the terminal using](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) `print(“\033c")`
    * [Restarting Python script using](https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself) `os.execv(sys.executable, ['python'] + sys.argv)` 

* [Bobby Handz Blog](https://bobbyhadz.com/blog/python-importerror-cannot-import-name) - Shows reason and solution to my issue on `ImportError: cannot import name 'Game' from partially initialized module 'game_manager' (most likely due to a circular import)`.

[Back to Table of Contents](#table-of-contents)

## ACKNOWLEDGMENT
* Ms Daisy McGirr, my Code Institute mentor, of her guidance and valuable suggestions in this project.
* My wife, Kyle, for the full support especially as I burn the midnight oil.