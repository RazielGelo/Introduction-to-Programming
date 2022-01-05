# Python Functions

# def say_a_name(name="nobody", age=100):
#     print(f"Hello {name} you are {age} years old.")

# say_a_name('Joseph', 35)
# say_a_name()

"""
	1.) Below is a simple Python function that is created with errors. 
	Uncomment the code, fix the errors and make sure that the function 
	is called.
"""
print("\nQ 1.")


def sayHello():
    print("Hello World")


sayHello()


"""
	2.) Below is a Python function that uses parameters that is created
	with errors. Uncomment the code, fix the errors and call the function
	twice using the parameters 
"""
print("\nQ 2.")


def divideNumberBy(num, divider):
    result = round(num / divider, 2)
    print(f"{num} divided by {divider} is {result}")


divideNumberBy(10, 2)


"""
	3.) Write a function that takes in 2 parameters. Both of these parameters
	should be numbers. Return a number that is both of the parameters multiplied
	together. If a parameter is not given then set its default value to be 0. 
	Test this function out on the following and call the function in
	a print() so that we can see the result:
	5, 5
	10, 7
	-12, 4
	8
"""
print("\nQ 3.")


def multiply_num(num1=0, num2=0):
    return round(num1 * num2, 2)


print(multiply_num(5, 5))
print(multiply_num(10, 7))
print(multiply_num(-12, 4))
print(multiply_num(8))


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

def concat_multiple_words(word, repeat):
    repeated_word = ""
    for iteration in range(repeat):
        repeated_word += word
        
    return repeated_word 

print(concat_multiple_words("Vancouver", 3))
print(concat_multiple_words("XoXo", 10))
    
    


"""
	5.) Below is a list of letters with some letters being present more
	than once. Write a function that takes in a list as a parameter and
	returns a list that is sorted and has no duplicate items. Print 
	lettersList after it has passed through the function e.g.
	print( funcName( lettersList ) )
"""
print("\nQ 5.")

lettersList = ["A", "B", "C", "D", "B", "A", "F", "C", "A"]

def list_converter(param_list):
    remove_duplicates = set(param_list)
    ordered_list = list(remove_duplicates)
    ordered_list.sort()    
    return ordered_list
    
print(list_converter(lettersList))
    


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

animalList = ["dog", "cat", "elephant", "dog",
              "tortoise", "cat", "dog", "horse", "elephant"]

def remove_item_from_list(param_list, item):
    while item in param_list:
        param_list.remove(item)
    return param_list

print (remove_item_from_list(animalList, "dog"))
    


"""
	7.) Create a function that takes in a string parameter and returns
	a dictionary that contains the following keys and respective values:
	"word": the string passed in
	"numberOfChars": number of characters in string
	"hasCapital": True or False whether string has a capital letter

	Test it out on the below variables
"""
print("\nQ 7.")

string1 = "planet"
string2 = "Hello"

def string_details(para_string):
    dict_details = {
        "word": para_string,
        "numberOfChars": len(para_string),
        "hasCapital": True if para_string[0].isupper() else False,
        # "hasAnyCapital": True if any(x.isupper() for x in para_string) else False
        }
    return dict_details

print(string_details(string1))
print(string_details(string2))


"""
	8.) Create a function that takes in a string parameter and returns
	a dictionary that contains the following keys and respective values:
	"word": the string passed in
	"numberOfChars": number of characters in string
	"hasCapital": True or False whether string has a capital letter

	Create a function that takes in a list of strings and returns
	a new list that contains strings that are greater than 4 characters
	long and contain at least one capital letter.
	Hint: use the function you created above to help you here.
"""
print("\nQ 8.")

wordsList = ["cat", "Monday", "Top", "help", "moNster", "lakE"]

def filter_list(para_list):
    new_list = []
    for items in para_list:
        if len(items) > 4 and any(x.isupper() for x in items):
        	new_list.append(items)
    return new_list

print(filter_list(wordsList))


