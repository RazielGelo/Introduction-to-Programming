# Hangman (Procedural Programming) Imperative / Structured
# https://deepsource.io/glossary/procedural-programming/
from random import randrange

def start_game():
	global game_word, guess_word, guess_num, guess_total, guess_attempts
	game_word = get_random_word()
	guess_word = display_guess_word(game_word, [])
	guess_num = 0
	guess_total = 6
	guess_attempts = []
	game_turn()


def get_random_word():
	words = ["animal", "house", "canada", "world", "bank", "marriage", "solar"]
	word = words[randrange(len(words))]
	return word.lower()


def display_guess_word(game_word, prev_guesses = []):
	# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
	player_word = [letter if letter in prev_guesses else '_' for letter in game_word]
	"""
	player_word = []

	for letter in game_word:
		if letter in prev_guesses:
			player_word.append(letter)
		else:
			player_word.append('_')
	"""
	return ''.join(player_word)


def game_turn():
	global guess_word, guess_num, guess_attempts

	# ask user for input
	print(f"\n{guess_num}/{guess_total} Guess a letter\n{' '.join(guess_word)}")
	
	user_letter = input("Pick letter: ")
	guess_attempts.append(user_letter)

	new_guess_word = display_guess_word(game_word, guess_attempts)
	if new_guess_word != guess_word:
		guess_word = new_guess_word
	else:
		guess_num += 1

	game_event(guess_word, guess_num)


def game_event(guess_word, guess_num):
	# Check if game has been won
	if '_' in guess_word:
		# Check if game is over
		if guess_num > guess_total:
			print(f"\nGame Over :(\nThe word was '{game_word}'")
		# Continue playing game
		else:
			game_turn()
	else:
		# Game has been won
		print(f"\n{guess_num}/{guess_total} Well Done!\nThe word was '{game_word}'")


start_game()