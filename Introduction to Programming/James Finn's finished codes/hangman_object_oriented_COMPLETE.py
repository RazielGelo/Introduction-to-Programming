# Hangman (Object-Oriented Programming)
# https://deepsource.io/glossary/object-oriented-programming/
from random import randrange

class WordMethods:
	def __init__(self):
		pass

	def get_random_word(self):
		words = ["animal", "house", "canada", "world", "bank", "marriage", "solar"]
		word = words[randrange(len(words))]
		return word.lower()

	def display_guess_word(self, game_word, prev_guesses = []):
		# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
		player_word = [letter if letter in prev_guesses else '_' for letter in game_word]
		return ''.join(player_word)


class Hangman:
	def __init__(self):
		self.game_word = ''
		self.guess_word = ''
		self.guess_num = 0
		self.guess_total = 6
		self.guess_attempts = []


	def start_game(self):
		self.game_word = word_methods.get_random_word()
		self.guess_word = word_methods.display_guess_word(self.game_word, [])
		self.guess_num = 0
		self.guess_total = 6
		self.guess_attempts = []
		self.game_turn()


	def game_turn(self):
		# ask user for input
		print(f"\n{self.guess_num}/{self.guess_total} Guess a letter\n{' '.join(self.guess_word)}")
		
		user_letter = input("Pick letter: ")
		self.guess_attempts.append(user_letter)

		new_guess_word = word_methods.display_guess_word(self.game_word, self.guess_attempts)
		if new_guess_word != self.guess_word:
			self.guess_word = new_guess_word
		else:
			self.guess_num += 1

		self.game_event(self.guess_word, self.guess_num)


	def game_event(self, guess_word, guess_num):
		# Check if game has been won
		if '_' in guess_word:
			# Check if game is over
			if guess_num > self.guess_total:
				print(f"\nGame Over :(\nThe word was '{self.game_word}'")
			# Continue playing game
			else:
				self.game_turn()
		else:
			# Game has been won
			print(f"\n{guess_num}/{self.guess_total} Well Done!\nThe word was '{self.game_word}'")


word_methods = WordMethods()
game = Hangman()


game.start_game()