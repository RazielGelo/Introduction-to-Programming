# Python Functions

"""
	1.) Below is a simple Python function that is created with errors. 
	Uncomment the code, fix the errors and make sure that the function 
	is called.
"""
print("\nQ 1.")

def say_hello():
	print("Hello World")

say_hello()



"""
	2.) Below is a Python function that uses parameters that is created
	with errors. Uncomment the code, fix the errors and call the function
	twice using the parameters 
"""
print("\nQ 2.")

def divide_number_by(num, divider):
	result = round(num / divider, 2)
	print(f"{num} divided by {divider} is {result}")

divide_number_by(7, 2)



"""
	3.) Write a function that takes in 2 parameters. Both of these parameters
	should be numbers. Return a number that is both of the parameters multiplied
	together. Test this function out on the following and call the function in
	a print() so that we can see the result:
	5, 5
	10, 7
	-12, 4
"""
print("\nQ 3.")

def multiply_numbers(num1, num2):
	result = num1 * num2
	return result

print( multiply_numbers(5, 5) )
print( multiply_numbers(10, 7) )
print( multiply_numbers(-12, 4) )



"""
	4.) Write a Python function that takes in 2 parameters, The first is 
	a string and the second is a number. Make this function return a new
	string that contains the first string printed the number of times as
	the second parameter dictated e.g. 'James', 3 would return
	'JamesJamesJames'
	Call this function on the following sets of parameters and print the 
	result to the console.
	Vancouver, 3
	XoXo, 10

"""
print("\nQ 4.")

def multiply_words(string, num):
	result = ''
	for n in range(num):
		result += string
	return result

multiply_words('Vancouver', 3)
multiply_words('XoXo', 10)



"""
	5.) Below is a list of letters with some letters being present more
	than once. Write a function that takes in a list as a parameter and
	returns a list that is sorted and has no duplicate items. Print 
	lettersList after it has passed through the function e.g.
	print( funcName( lettersList ) )
"""
print("\nQ 5.")

lettersList = ["A", "B", "C", "D", "B", "A", "F", "C", "A"]

def return_no_duplicate_list(letters):
	noDuplicates = set(letters)
	noDuplicates = list(noDuplicates)
	noDuplicates.sort()

	return noDuplicates

print( return_no_duplicate_list(lettersList) )



"""
    6.) Write a function that takes in 2 parameters. The first is a list. 
    The second should be a string. The function should remove all items
    from the list that are equal to the second parameter e.g.
    list = ['A','A','B','B','C']
    second parameter = 'A'

    returned list = ['B','B','C']

    Remove all occurences of "dog" from the animalList and print out
    the new "dog" free list.

"""
print("\nQ 6.")

animalList = ["dog", "cat", "elephant", "dog", "tortoise", "cat", "dog", "horse", "elephant"]

def remove_all_items(listPara, stringPara):
    while stringPara in listPara:
        listPara.remove(stringPara)
    return listPara

print( remove_all_items(animalList, "dog") )



"""
	7.) Create a function that takes in a string parameter and returns
	a dictionary that contains the following keys and respective values:
	{
		"word": the word itself
		"numberOfChars": the number of characters in the word
		"hasCapital": True or False based on whether the word has a capital letter
	}
"""
print("\nQ 7.")

string1 = "planet"
string2 = "Math"

def string_details(word):
	length = len(word)
	hasCapital = word.islower()
	return {
		"word": word, 
		"numberOfChars": length, 
		"hasCapital": not hasCapital
	}


print( string_details(string1) )
print( string_details(string2) )



"""
	8.) Create a function that takes in a list of words. Return a new
	list containing only the words that contain more than 4 characters
	and also have a capital letter
	You can use the previous question to help you in this regard.
"""
print("\nQ 8.")

wordsList = ["cat", "Monday", "Top", "help", "moNster", "lakE"]

def only_big_cap_strings(stringList):
	onlyBigCapStringsList = []

	for w in stringList:
		sDetails = string_details(w)

		if sDetails["numberOfChars"] > 4 and sDetails["hasCapital"] == True:
			onlyBigCapStringsList.append(w)

	return onlyBigCapStringsList

print( only_big_cap_strings(wordsList) )