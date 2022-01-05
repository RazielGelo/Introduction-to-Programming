# Python Assignment 5
import assignment5ModuleContainingVariables as mod

"""
    1.) Making a Tuple of Numbers
    Write a function called 

    divisible_numbers() 

    that takes in two number parameters. The first parameter
    represents the start number and the second represents the end number.
    This function should return a tuple of all the numbers between these
    numbers (including the start and end numbers themselves if applicable) 
    that are divisible by either the number 3, 5 or 7. That means if I divide 
    the number by either 3 or by 5 or by 7 it shouldn't leave a remainder.
    The modulo operator % will come in handy here https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    as will using casting to transform a collection of one type into another.
    
    EXAMPLE
    ParameterA = 2,  ParameterB = 14, Result = (3, 5, 6, 7, 9, 10, 12, 14)
    ParameterA = -5, ParameterB = 5 , Result = (-5, -3, 0, 3, 5)
"""
print("\nQ 1.")

def divisible_numbers(start, end):
    num_list = []
    for i in range(start, end+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            num_list.append(i)

    return tuple(num_list)

print(divisible_numbers(-5, 5))
print(divisible_numbers(0, 25))
print(divisible_numbers(490, 519))



"""
	2.) Write a function called 

    no_hyphen_only_lower() 

    that takes in a string as a parameter. This function 
    should return a boolean True if the string contains only lowercase letters
    and does not contain a hyphen "-".
    It should return False if there are any uppercase letters present or if 
    there are any hyphens "-" present.
    EXAMPLE
    Parameter = "james",     Result = True
    Parameter = "Mark",      Result = False
    Parameter = "ann-marie", Result = False

    Use this function to count the number of items in the question_two_multi_list
    variable that is stored in the accompanying module that contain only lowercase 
    letters without any hyphens. Each list item is a single word or single hyphenated word.

    Finally print a sentence that reads "There are X lowercase no-hyphen words
    in the list" where X is the counted number.

    EXAMPLE
    test_list = [
        ["bakery", "Lions", "ice-cream", "caT", "sunday", "marKET"],
        ["drive-through", "Inspired", "haze"]
    ]
    Result = "There are 3 lowercase no-hyphen words in the list"

"""

print("\nQ 2.")

def no_hyphen_only_lower(word):
    return True if word == word.lower() and "-" not in word else False

count_lower = 0
for lists in mod.question_two_multi_list:
    for word in lists:
        if no_hyphen_only_lower(word):
            count_lower += 1

print(f"There are {count_lower} lowercase no-hyphen words in the list")



"""
    3.) Write a function called 

    most_used_words() 

    that takes in
    a string as a parameter and returns a dictionary containing
    any word that appears more than 4 times in the string. The
    word should be in lowercase and appear as the the dictionary key 
    and its value should be
    an integer representing the amount of times it appears. The
    order these words appear in the dictionary does not matter.
    The casing of the word should not matter either e.g. cat is
    the same as CAT and should be counted together.

    Use this function to return a dictionary on the snippet
    of text from the 1840 Canadian Act of Union which is 
    stored in the accompanying module.
    
    EXAMPLE
    Parameter = "Cat story. The cat in the cat ville, had the sister cat, who's name was the cat-like name called Cat. All the cats loved being a cat.",     
    Result = {'cat': 6, 'the': 5}

    NOTE in the code above cat-like was not considered cat neither
         was cats because of the s at the end. 

"""

print("\nQ 3.")

def most_used_words(txt):
    word_dict = {}
    txt_list = txt.split()
    for word in txt_list:
        word = word.lower().rstrip(',.!')
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    final_word_count = {}
    for w in word_dict:
        if word_dict[w] > 4:
            final_word_count[w] = word_dict[w]

    return final_word_count

print(most_used_words(mod.the_union_act_1840))
print(most_used_words("Hello World"))
print(most_used_words("We declare the count state variable, and then we tell React we need to use an effect we we We. We pass a function to the useEffect Hook."))
print(most_used_words("Cat story. The cat in the cat ville, had the sister cat, who's name was the cat-like name called Cat. All the cats loved being a cat."))