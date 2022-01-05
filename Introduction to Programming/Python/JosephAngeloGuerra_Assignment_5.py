# Python Assignment 5
#
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_5.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the accompanying module file
# assignment5ModuleContainingVariables.py

"""
    1.) Making a Tuple of Numbers
    Write a function called 

    divisible_numbers() 

    that takes in two number parameters. The first parameter
    represents the start number and the second represents the end number.
    The first parameter will always be smaller than the second parameter
    so there is no need to check or constrain this.
    This function should RETURN a tuple of all the numbers between these
    numbers (including the start and end numbers themselves if applicable) 
    that are divisible by either the number 3, 5 or 7. That means if I divide 
    the number by either 3 or by 5 or by 7 it shouldn't leave a remainder.
    The modulo operator % will come in handy here https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    as will using casting to transform a collection of one type into another.
    
    EXAMPLE
    ParameterA = 2,  ParameterB = 14, Result = (3, 5, 6, 7, 9, 10, 12, 14)
    ParameterA = -5, ParameterB = 5 , Result = (-5, -3, 0, 3, 5)
"""
import assignment5ModuleContainingVariables as assign5_module
print("\nQ 1.")


def divisible_numbers(num_start, num_end):
    # Initialize list to contain range of inputted numbers.
    list_range = []

    # Added +1 to include num_end in the range.
    for i in range(num_start, num_end+1):

        # conditional to output only numbers that are divisible by 3,5 or 7.
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            list_range.append(i)

    # Cast list into tuple
    tuple_range = tuple(list_range)
    return tuple_range


print(divisible_numbers(2, 14))
print(divisible_numbers(-5, 5))


"""
	2.) Returning True or False

    no_hyphen_only_lower() 

    that takes in a string as a parameter. This function 
    should RETURN a boolean True if the string contains only lowercase letters
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

    Finally PRINT a sentence that reads "There are X lowercase no-hyphen words
    in the list" where X is the counted number.

    EXAMPLE
    test_list = [
        ["bakery", "Lions", "ice-cream", "caT", "sunday", "marKET"],
        ["drive-through", "Inspired", "haze"]
    ]
    Result = "There are 3 lowercase no-hyphen words in the list"

"""
print("\nQ 2.")


# Function to check if string is lowercase and if it has a hyphen.

def no_hyphen_only_lower(para_string):
    if para_string.islower() and "-" not in para_string:
        return True
    else:
        return False


# Initialization of Variables
multi_list = assign5_module.question_two_multi_list
counter = 0

# Loop through Outer Lists
for outer_list in multi_list:

    # Loop through items inside Outer Lists
    for items in outer_list:

        # Usage of function above to count for strings that meet the criteria.
        if no_hyphen_only_lower(items):
            counter += 1

print(f"There are {counter} lowercase no-hyphen words in the list.")


"""
    3.) Dictionary of Counted Words

    most_used_words() 

    that takes in a string as a parameter and returns a dictionary containing
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

    NOTE in the code above, "cat-like" was not considered "cat" neither
         was "cats" because of the "s" at the end. 

"""
print("\nQ 3.")

# Simplying the variable from assignment module variable "the_union_act_1840".
sample = assign5_module.the_union_act_1840

def most_used_words(para_string):
    # Support for regular expressions.
    import re

    # Initialization of two dictionaries original and filtered.
    occurences = dict()
    filtered_occurences = dict()

    # List wherein words are lower cased and split with each other, removing punctuations.
    # words = para_string.lower().replace(",", "").replace(".", "").split()

    # Same as above code but covers more bases.
    word_list = re.sub("[^\w\s]", "", para_string.lower()).split()

    # Loop to add key and count it's occurences.
    # for word in word_list:
    #     if word in occurences:
    #         occurences[word] += 1
    #     else:
    #         occurences[word] = 1

    # Loop to filter key and it's occurences based on given criteria.
    # for (key, value) in occurences.items():
    #     if value > 4:
    #         filtered_occurences[key] = value
    # return filtered_occurences
    
    
    for key in word_list:
        if word_list.count(key) > 4:
            # Used filtered_occurences[key] filtered by word_list.count(i)
            filtered_occurences[key] = word_list.count(key)
    return filtered_occurences

    # # Simplied counter for iteration of strings in a list.
    # for i in word_list:
    #     filtered_occurences[i] = word_list.count(i)
    # return filtered_occurences
            

print(most_used_words(sample))
