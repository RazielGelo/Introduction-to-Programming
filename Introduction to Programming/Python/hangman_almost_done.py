# Hangman
from random import randrange

print("You are playing Hangman")

def return_random_word():
    words = ["world", "goodbye", "hello"]
    word = words[randrange(len(words))]
    return word.lower()

def display_guess_word(prev_guesses=[]):
    guess_word = ""

    # add hyphen to string for each letter in correct_word
    # add letter to string for each correct letter in correct_word
    for letter in correct_word:
        if letter in prev_guesses:
            guess_word += letter
        else:
            guess_word += "_"

    # return hyphen_string word
    return " ".join(guess_word)

guess_limit = 6
guess_counter = 0
correct_word = return_random_word()
guessed_attempts = []

#print(display_guess_word())
print(correct_word)

def game_turn():
    global guess_counter
    print(f"{guess_counter} / {guess_limit}\n{display_guess_word(guessed_attempts)}")
    user_letter = input("Pick a letter: ").lower()
    guessed_attempts.append(user_letter)

    # increment guess_counter if guess is wrong
    if user_letter not in correct_word:
        guess_counter += 1 

    if "_" in display_guess_word(guessed_attempts):
        # Game Continues
        if guess_counter <= guess_limit:
            # Start another turn
            game_turn()
        else:
            # Game Over
            print("You Lose!")
    else:
        # Game has been won!
        print("You WON!!! " + correct_word)

    
   
game_turn()

# for i in range(6):
#     game_turn()