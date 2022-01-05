# Python Loops

"""
	1.) Below is a tuple, list and dictionary. Write a simple for loop
	that prints off each value in each of them
"""
print("\nQ 1.")

myList = ["list1", "list2"]
myTuple = ("tuple1", "tuple1")
myDict = {"A": "word", "B": 1, "C": 3}

for item in myList:
	print(item)

#[print(item) for item in myList]

for item in myTuple:
	print(item)

for key in myDict:
	print(myDict[key])



"""
	2.) Loop through this string and for each character print out
	"x is a letter in y" where x is the letter and y is the contents
	of the string
"""
print("\nQ 2.")

myString = "abcd"

for letter in myString:
	print(f"{letter} is a letter in {myString}")



"""
	3.) Loop through this string and using a single print(), print
	out the string but have all vowels capitalized. You'll need to
	create a new empty string and add each letter. If the letter is
	a vowel use .upper() to uppercase it
"""
print("\nQ 3.")

myOtherString = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
vowelsCap = ""

for letter in myOtherString:
	#if letter == 'a' or letter == 'e' or letter == 'i':
	if letter in vowels:
		vowelsCap += letter.upper()
	else:
		vowelsCap += letter

print(vowelsCap)



"""
	4.) Write a for loop that prints the numbers from 0 to 5
"""
print("\nQ 4.")

for num in range(0, 6):
	print(num)



"""
	5.) Write a for loop that prints the numbers from 5 to 20
	in increments of 3. That is to print 5 8 11 14 17 20. Make
	sure to print this all off in a single print()
"""
print("\nQ 5.")

msg = ""
for num in range(5, 21, 3):
	msg += f'{num} '
print(msg)



"""
	6.) Create a new list that contains only the planet strings
	from planetList that have 5 characters or less.
"""
print("\nQ 6.")

planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
shortPlanets = []

for planet in planetList:
	if len(planet) <= 5:
		shortPlanets.append(planet)

print(shortPlanets)

shortHandPlanets = [ p for p in planetList if len(p) <= 5 ]
print(shortHandPlanets)



"""
	7.) Write code that removes all items from the list that are
	'N'. Decide on what loop is best to use in thie situation. Also
	count how many times 'N' appears in the list. Finally print the
	new list and print "X number of Ns were removed from the list"
"""
print("\nQ 7.")

listToRemoveItems = ['N', 'A', 'B', 'N', 'N', 'M', 'B', 'W', 'A', 'N', 'L', 'S', 'H', 'D', 'N', 'N', 'P']
nCount = 0

while 'N' in listToRemoveItems:
	listToRemoveItems.remove('N')
	nCount += 1

print(listToRemoveItems)
print(str(nCount) + ' numbers of N were removed from list')

# Doing it the below way is wrong because you are looping through
# a list at the same time you're changing its length by removing
# elements. Therefore the loop skips over certain items and as
# a result not all 'N's are found and removed
listToRemoveItems2 = ['N', 'A', 'B', 'N', 'N', 'M', 'B', 'W', 'A', 'N', 'L', 'S', 'H', 'D', 'N', 'N', 'P']
for char in listToRemoveItems2:
	print(char)
	if char == 'N':
		listToRemoveItems2.remove('N')
	
print(listToRemoveItems2)
# ==================================



"""
	8.) Write code that asks the user to input a number. If they
	don't input a number, keep asking them to do it until they
	do. When they do, print the sentence "Half of your number is X"
	where X is half of the number.
	Use a while loop. Use try...except to test if input is an int
"""
print("\nQ 8.")

userNumber = ""

while type(userNumber) is not int:
	userNumber = input("Input a number: ")

	try:
		userNumber = int(userNumber)
	except:
		print("Please enter a number!")

print(f"Half of your number is {userNumber/2}")
