# Programming Paradigms


# Procedural Programming
# =============================================
num_list = [1,2,3,4,5,6]

def square_number_list(nums):
	square_list = []
	for num in nums:
		square_list.append(num * num)

	return square_list

num_squared_list = square_number_list(num_list)

print(f'{num_squared_list} Procedural')


# =============================================


# Object-Oriented Programming
# =============================================
class SquareNumbers:
	def __init__(self):
		self.num_squared_list = []

	def square_num_list(self, nums):
		square_list = []
		for num in nums:
			square_list.append(num * num)

		self.num_squared_list = square_list

num_obj = SquareNumbers()
num_obj.square_num_list([1,2,3,4,5,6])

print(f'{num_obj.num_squared_list} OOP')
# =============================================


# Functional Programming
# =============================================
def square_num(num):
	square_num = num * num
	return 

def square_list(num_list):
	return list(map(square_num, num_list))

print(f'{square_list([1,2,3,4,5,6])} Functional')
# =============================================

