# Python Assignment 4
import book

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
# Place book contents in string variable
text = book.paragraphs

# Count . and spaces to track sentences and words
msg = f"There are {text.count('.')} sentences in book.\n"
msg += f"There are {text.count(' ') + 1} words in book.\n"

# Get start index position of last sentence by finding last
# occurrence of a space. Use slice to get sentence and
# replace all "and" with "&"
lastSentencePos = text.rfind('. ')
lastSentence = text[lastSentencePos + 2:]
msg += lastSentence.replace("and", "&")

print(msg)


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

    Gross Salary = 400, Bracket = Low,    Tax = 0,     Child Benefits = 20, Net Income = 420, Number of Kids = 2
    Gross Salary = 620, Bracket = Medium, Tax = 18,    Child Benefits = 0,  Net Income = 602
    Gross Salary = 905, Bracket = High,   Tax = 81.25, Child Benefits = 0,  Net Income = 823.75
"""

print("\nQ 2.")

grossSalary = input("What is your gross salary? ")

try:
    # Check if grossSalary is a number
    grossSalary = float(grossSalary)
    tax = 0
    childBenefits = 0
    bracket = "Low"

    # Low Tax Bracket
    if grossSalary < 500:
        bracket = "Low"
        numOfKids = input("How many children do you have? ")

        # Check if user inputted number for kids
        try:
            childBenefits = 10 * int(numOfKids)
        except:
            pass

    # Medium Tax Bracket
    elif grossSalary >= 500 and grossSalary < 700:
        bracket = "Medium"
        tax += (grossSalary - 500) * .15

    # High Tax Bracket
    else:
        bracket = "High"
        tax += (700 - 500) * .15
        tax += (grossSalary - 700) * .25

    print(f"""Gross Income = {grossSalary}
Tax Bracket = {bracket}
Total Tax = {tax}
Child Benefits = {childBenefits}
Net Income = {grossSalary - tax + childBenefits}""")

except:
    print("ERROR please enter a number")
