# Hangman
from random import randrange

print("You are playing Hangman")

# 1. Stop game from incrementing guess_counter if user
#    types in same letter as before
# 2. Use bigger collection of words in game. Import module
#    of words.
# 3. When game has ended ask user if they want to play again
# 4. Draw the hangman or life bar

# Global Variables
correct_word = ""
guess_limit = 6
guess_counter = 0
guessed_attempts = []
debugger = True


def start_game():
    """
    It initialises the game and assigned random word for correct_word

    :return: None
    """
    global correct_word 
    correct_word = return_random_word()
    if debugger == True:
        print(correct_word)
    game_turn()


def return_random_word():
    """
    Returns a random, lowercase word from text file

    :return: {string} contain _ and letters of correct_word
    """

    with open('book.txt', mode='r', encoding='utf-8') as f:
        all_text = f.read()
    
    # break text into words
    all_words = all_text.split()
    filtered_words = []

    for w in all_words:
        # Remove all punctuation
        w = w.strip(',.!:').replace("'", "").lower()
        # Select only long words
        if len(w) > 4 and '-' not in w:
            filtered_words.append(w)

    # Remove duplicates
    filtered_set = set(filtered_words)
    filtered_list = list(filtered_set)

    if debugger:
        print('filtered_list')
        print(filtered_list)

    #words = ["world", "goodbye", "hello", "hello", "hello", "hello"]
    #word = words[randrange(len(words))]
    
    return filtered_list[randrange(len(filtered_list))]


def display_guess_word(prev_guesses=[]):
    """
    Takes in a list of all previous guessed letters and returns 
    a string showing correct letters and underscores for not 
    identified letters

    :params: prev_guesses {list} contains char for each previous guessed letter
    :return: {string} the displayed guess word
    """
    guess_word = ""
 
    for letter in correct_word:
        # add _ to string for each not guessed letter in correct_word
        if letter in prev_guesses:
            guess_word += letter
        # add letter to string for each correct letter in correct_word
        else:
            guess_word += "_"

    # return hyphen_string word
    return " ".join(guess_word)


def game_turn():
    """
    Takes in user letter and increments guess_counter if user failed.
    Checks the state of the game after each turn

    :return: None
    """
    global guess_counter

    # Display game turn to user
    print(f"{guess_counter} / {guess_limit}\n{display_guess_word(guessed_attempts)}")
    
    # Get user letter input
    user_letter = input("Pick a letter: ").lower()

    # increment guess_counter if guess is wrong
    if user_letter not in correct_word and user_letter not in guessed_attempts:
        guess_counter += 1 

    # Add user's letter to previous guesses list
    guessed_attempts.append(user_letter)

    # Check to see game state
    check_game_state()


def check_game_state():
    """
    Checking to see if game is won, lost or should continue
    and enforces those states.

    :return: None
    """

    if "_" in display_guess_word(guessed_attempts):
        # Game Continues
        if guess_counter <= guess_limit:
            # Start another turn
            game_turn()
        else:
            # Game Over
            print("You Lose!")
            restart_game()
    else:
        # Game has been won!
        print("You WON!!! " + correct_word)
        restart_game()


def restart_game():
    global guessed_attempts, guess_counter

    print('Do you want to restart the game?')

    user_decision = input('Y = yes, N = no: ').upper()

    if user_decision == 'Y':
        guess_counter = 0
        guessed_attempts = []
        start_game()

# Start up the game
start_game()