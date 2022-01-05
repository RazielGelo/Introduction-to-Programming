# Python Loops

# myString = 'VancouverCommunityCollege'
# newString = ''
# for char in myString:
#     newString += char + '_'

# print(newString)  

# colorList = ['blue', 'red', 'green',]  
# for color in colorList:
#     print(color)
    
# for num in range(20, 10, -1):
#     print(num)
# else:
#     print('Loop has ended.')
    
# for num in range(20):
#     if num % 2 == 0:
#         print(num)
# else:
#     print('Loop has ended.')
    
# # Versus

# for num in range(10):
#     if num % 2 == 0:
#         continue
#     print(num)
# else:
#     print('Loop has ended.')
    

# counter = 0
# while counter < 11:
#     print(f'counter = {counter}')
#     counter += 1

"""
	1.) Below is a tuple, list and dictionary. Write a simple for loop
	for each one, that prints off each value in each of them
"""
from math import e


print("\nQ 1.")

myList = ["list1", "list2"]
myTuple = ("tuple1", "tuple2")
myDict = {"A": "word", "B": 1, "C": 3}

for value in myList:
    print(value)

for value in myTuple:
    print(value)
    
for key in myDict:
	print(key, myDict[key])



"""
	2.) Loop through this string and for each character print out
	"x is a letter in y" where x is the letter and y is the contents
	of the string
"""
print("\nQ 2.")

myString = "abcd"

for letter in myString:
    print(f"{letter} is a letter in {myString}.")



"""
	3.) Loop through this string and using a single print(), print
	out the string but have all vowels capitalized. You'll need to
	create a new empty string and add each letter. If the letter is
	a vowel use .upper() to uppercase it
"""
print("\nQ 3.")

myOtherString = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
uppercaseVowels = ''

for letter in myOtherString:
    # if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    if letter in vowels:
        uppercaseVowels += letter.upper()
    else:
        uppercaseVowels += letter
print(uppercaseVowels)
        
        
"""
	4.) Write a for loop that prints the numbers from 0 to 5
"""
print("\nQ 4.")

for num in range(6):
    print(num)



"""
	5.) Write a for loop that prints the numbers from 5 to 20
	in increments of 3. That is to print 5 8 11 14 17 20. Make
	sure to print this all off in a single print()
"""
print("\nQ 5.")

allNum = ''

for num in range(5, 21, 3):
    allNum += str(num) + ' '
print(allNum)



"""
	6.) Create a new list that contains only the planet strings
	from planetList that have 5 characters or less. Print out
	that list at the end.
"""
print("\nQ 6.")

planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
fivecharList = []

for planets in planetList:
    if len(planets) <= 5:
         fivecharList.append(planets)
print(fivecharList) 

shortHandPlanets = [p for p in planetList if len(p) <= 5]
print(shortHandPlanets)

"""
	7.) Write code that removes all items from the list that are
	'N'. Decide on what loop is best to use in this situation. Also
	count how many times 'N' appears in the list. Finally print the
	new list and print "X number of Ns were removed from the list"
"""
print("\nQ 7.")

listToRemoveItems = ['N', 'A', 'B', 'N', 'N', 'M', 'B', 'W', 'A', 'N', 'L', 'S', 'H', 'D', 'N', 'N', 'P']
newList = []

nCount = 0

while "N" in listToRemoveItems:
    listToRemoveItems.remove("N")
    newList = listToRemoveItems    
    nCount += 1
print(f'''This is the new list: {newList}
{nCount} number of Ns were removed from the list.''')

"""
	8.) Write code that asks the user to input a number. If they
	don't input a number, keep asking them to do it until they
	do. When they do, print the sentence "Half of your number is X"
	where X is half of the number.
	Use a while loop. Use try...except to test if input is an int
"""
print("\nQ 8.")

inputNumber = ""

while inputNumber == "":
	try:
		inputNumber = int(input("Please enter a number: "))
	except:
		print("Please enter a valid number.")
else:
	print(f"Half of your number is {inputNumber / 2}.")

# Tree loop
 
print("\nQuestion Tree Loop.")

msg = ""
tree_level = int(input("Please enter a number for your tree height: "))
# Loop starts at index 1
for height in range(tree_level + 1):
    msg += "\n"
    # If tree_level = 5 then height = 1 then 5-1 = 4  
    for space in range(tree_level - height):
        msg += " "
    # Incrementing number of asterisk
    for asterisk in range((2*height)-1):  
        msg += "*"
    
print(msg)

