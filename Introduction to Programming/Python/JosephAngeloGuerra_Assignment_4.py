# Python Assignment 4
#
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_4.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the book.py file
import book as pybook
import math
"""
    1.) A file called book.py is included in this folder. It contains
    a string variable called paragraphs. Write code to do the following:
    - Import the book file as a module into this file

    In a single message print the following:
    - "There are X sentences in book."
    - "There are Y words in book."
      Note that hyphenated words e.g. "backward-compatible" count
      as a single word and names, numbers and years count as
      words as well.
    - The last sentence from paragraph but replace all occurences
      of the word "and" with "&".
"""

print("\nQ 1.")
# Count sentences
countSentence = pybook.paragraphs.count(".")
# Count words
countWords = len(pybook.paragraphs.split())
# Organize and split sentences into a list.
sentenceList = list(pybook.paragraphs.split(". "))
# Get last sentence by using sentenceList as an array and replace "and" with "&".
lastSentence = sentenceList[len(sentenceList)-1].replace("and", "&")

# Loop to get the number of sentence - just playing with loop in python
# for x in pybook.paragraphs:
#     if x == ".":
#       countSentence += 1

print(f'''
There are {countSentence} sentences in book.
There are {countWords} words in book.
{lastSentence}''')


"""
	2.) Tax Collector

	Write code that will ask the user, using an input, what their
    monthly gross income is. If the user doesn't type in a number
    print "ERROR not a number" and do not proceed with
    the calculation.

    - If the user earns less than 500 dollars, the tax
    taken is 0 and they are in the low tax bracket. Only for these
    people should you do the following. Ask the user how many
    children they have. For each child that they have, give them
    10 dollars in child benefits. If the user does not type in a
    number they get 0 dollars in child benefits.

    - If the user earns 500 dollars or more but less than
    700 they are in the medium tax bracket. Tax taken
    here should be 15% of any sum that is over 500.

    - If the user earns 700 dollars or more they are in the high
    tax bracket. Tax taken here should be 15% of the sum that is
    over 500 but less than 700 and 25% of everything over 700.

    The final result should show in a single print the user's
    gross income, the tax bracket (low, medium or high), total
    tax, child benefits and net income (gross + child benefits -
    tax).

    Gross Salary = 400, Bracket = Low,    Tax = 0,     Child Benefits = 20, Net Income = 420, this user has 2 kids
    Gross Salary = 620, Bracket = Medium, Tax = 18,    Child Benefits = 0,  Net Income = 602
    Gross Salary = 905, Bracket = High,   Tax = 81.25, Child Benefits = 0,  Net Income = 823.75
"""

print("\nQ 2.")
# Initiation of variables
userSalary = input("Please enter your monthly gross income: ")
tax = 0
childBenefits = 0
bracket = ""
msg = ""
extMsg = ""

# Trying to catch if the user enters a wrong input type for gross income.
try:
    userSalary = float(userSalary)
except:
    print("ERROR not a number.")
else:
    # Low tax bracket
    if userSalary < 500:
        bracket = "Low"
        numOfKids = input("Please enter how many children you have: ")
        # Trying to catch if the user enters a wrong input type for number of children.
        try:
            numOfKids = abs(math.floor(float(numOfKids)))
        except:
            numOfKids = 0
        childBenefits += 10 * numOfKids
        extMsg = f"This user has {numOfKids} kids."
    # Medium tax bracket
    elif userSalary >= 500 and userSalary <= 700:
        bracket = "Medium"
        tax += (userSalary - 500) * 0.15
    # High tax bracket
    else:
        bracket = "High"
        tax += (700 - 500) * .15
        tax += (userSalary - 700) * .25
    msg = f'''
        Gross Income = {userSalary}
        Tax Bracket = {bracket}
        Total Tax = {tax}
        Child Benefits = {childBenefits}
        Net Income = {userSalary - tax + childBenefits}    
        '''
    # shorthand way to get a different output if tax bracket is low.
    print(msg + extMsg) if bracket == "Low" else print(msg)
    
