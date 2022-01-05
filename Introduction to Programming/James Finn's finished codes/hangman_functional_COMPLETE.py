# Hangman (Procedural Programming) Imperative / Structured
# https://deepsource.io/glossary/procedural-programming/
from random import choice

def start_game(guess_limit):
	game_turn(0, guess_limit, [], get_random_word())


def get_random_word():
	return choice(["animal", "house", "canada", "world", "bank", "marriage", "solar"]).lower()


def display_guess_word(game_word, prev_guesses = []):
	return ''.join([letter if letter in prev_guesses else '_' for letter in game_word])


def game_turn(guess_num, guess_limit, guess_attempts, game_word):
	# ask user for input
	print(f"\n{guess_num}/{guess_limit} Guess a letter\n{' '.join(display_guess_word(game_word, guess_attempts))}")
	
	guess_attempts.append(input("Pick letter: ").lower())

	if guess_attempts[-1] not in game_word:
		guess_num += 1

	game_event(guess_num, guess_limit, guess_attempts, game_word)


def game_event(guess_num, guess_limit, guess_attempts, game_word):
	# Check if game has been won
	if '_' in display_guess_word(game_word, guess_attempts):
		# Check if game is over
		if guess_num > guess_limit:
			print(f"\nGame Over :(\nThe word was '{game_word}'")
		# Continue playing game
		else:
			game_turn(guess_num, guess_limit, guess_attempts, game_word)
	else:
		# Game has been won
		print(f"\n{guess_num}/{guess_limit} Well Done!\nThe word was '{game_word}'")


start_game(6)