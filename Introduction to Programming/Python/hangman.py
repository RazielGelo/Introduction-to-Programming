# Hangman

import random
import re

print("You are playing Hangman!")

correct_word = ""
guess_limit = 6
guess_counter = 0
guessed_attempts = []


def start_game():
    global correct_word, guessed_attempts
    guessed_attempts = []
    correct_word = return_random_word()
    print(correct_word)
    game_turn()

def return_random_word():
    with open("book.txt", mode='r+', encoding='utf-8') as file:
        library = file.read()
        word_list = re.sub("[^\w\s]", " ", library.lower()).split()
        word_list = list(set(word_list))
    
    filtered_list = []
    for word in word_list:
        if len(word) > 4:
            filtered_list.append(word)
            
    print(filtered_list)
    
    word = random.choice(filtered_list)
    return word.lower()

def display_guess_word(prev_guesses=[]):
    # length of the correct_word
    guess_word = ""
    
    # add _ to string for each letter in correct_word
    for letter in correct_word:
        if letter in prev_guesses:
            guess_word += letter
        else:
            guess_word += "_"        
    
    # return hyphen_string word
    return " ".join(guess_word)

# print(correct_word)

def game_turn():
    global guess_counter
    
    # Display game turn to user
    print(f"{guess_counter} / {guess_limit}\n{display_guess_word(guessed_attempts)}\n")
    
    # Get user letter input
    user_letter = input("Pick a letter: ").lower()
    # Add user's letter to previous guesses list
    if user_letter in guessed_attempts:
        print(f"'{user_letter}' has been used. Please choose a different letter.")
    else:
        guessed_attempts.append(user_letter)
        # increment guess_counter if guess is wrong
        if user_letter not in correct_word:
            guess_counter += 1   
    
            
    check_game_state()

    
        
def check_game_state():
    # Checking to see if game is won, lost, or should continue
    if "_" in display_guess_word(guessed_attempts):
        # Game Continues
        if guess_counter <= guess_limit:
            # Start another turn
            game_turn()
        else:
            #Game Over
            print("You've lost!")
            restart_game()
    else:
        # Game has been won
        print("You've won!")
        restart_game()
    
def restart_game():
    global guessed_attempts, guess_counter
    
    print("Do you want to restart the game?")
    user_choice = input("Y = Yes, N = NO: ").upper()
    if user_choice == "Y":
        guess_counter = 0
        guessed_attempts = []
        start_game()
    else:
        print("Till next time!")

# Start up the game_turn()
start_game()







    
       
    




