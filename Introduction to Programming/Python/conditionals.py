# Python Conditionals

num = 0
name = "Angelo"

print(type(name))
print(type(num))

"""
	1.) Below, commented out, is an if else statement created with a
	lot of errors. Uncomment the code and fix the errors.
"""
print("\nQ 1.")

# Uncomment this code
if 5 < 10:
    print("5 is less than 10")

else:
    print("5 is greater than 10")


"""
	2.) Use the bool variable called isMorning below and write an if else
	statement that checks to see if isMorning is True. If it is True
	then print "Good Morning". If it is False then print "Good Evening".
"""
print("\nQ 2.")

isMorning = True

if isMorning:
    print("Good Morning.")
else:
    print("Good Evening.")


"""
	3.) Create a bool called isCanadian and assign it a boolean value.
	Create another bool called hasBlackHair and assign it a boolean value.
	Write a conditional statement that will print the sentence "You are
	Canadian and have black hair" if both bools are True. If not, don't
	print anything.
"""
print("\nQ 3.")

isCanadian = True
hasBlackHair = True

if isCanadian == True and hasBlackHair == True:
    print("You are Canadian and have black hair.")
else:
    print("")


"""
	4.) Ask the user to type in their name (input). Write code to check
	and see if their name:
	- is over 6 characters long
	- contains the letter "a"
	- contains the letter "c"
	If all of the above are true print "You have a long name that contains a and c"
"""
print("\nQ 4.")

# yourName = input("Please enter your name: ")

# if len(yourName) > 6 and "a" and "c" in yourName.lower():
# 	print("You have a long name that contains a and c.")
# else:
# 	print("You have a name shorter than 6 letters and doesn't have the letters a and c.")


"""
	5.) Create a string called day and assign it a value of one of
	the names of the day of the week e.g. "Wednesday". Write a
	conditional statement that will check your variable and print
	either "X is a work day" or "X is a weekend day" where X is
	your day variable.
"""
print("\nQ 5.")

# day = input("Please a day of the week: ").capitalize()

# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
# #if day == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday": This makes it always TRUE.
# 	print(f"{day} is a work day.")
# elif day == "Saturday" or day == "Sunday":
# 	print(f"{day} is a weekend day.")
# else:
# 	print(f"Please change the variable into something acceptable.")


"""
	6.) The variable below called currentHour represents an
	hour on the 24 hour clock e.g. either 0 - 23. It is currently
	commented out. Write code that
	asks the user to input a number between 0 and 23 to become
	currentHour. If this number cannot be turned into an int,
	automatically assign it the value of 0.

	Print the following based on the value of currentHour
	0 to 12 inclusive = "Morning time"
	13 to 16 inclusive = "Afternoon time"
	17 to 20 inclusive = "Evening time"
	21 to 23 inclusive = "Night time"
	any number < 0 or > 23 = "No time"

	Change the currentHour value to make sure all of your code
	is correct
"""
print("\nQ 6.")

currentHour = input("What hour (0-23) is it?: ")

try:
	currentHour = int(currentHour)

except:
	currentHour = 0

if currentHour >= 0 and currentHour <= 12:
	print("Morning Time")
elif currentHour >= 13 and currentHour <= 16:
	print("Afternoon Time")
elif currentHour >= 17 and currentHour <= 20:
	print("Evening Time")
elif currentHour >= 21 and currentHour <= 23:
	print("Night Time")
else:
	print("No time")



"""
	7.) Below is a nested conditional statement - one where ifs
	are inside other ifs. It is written with some errors. Uncomment
	the code and fix it so that it will work correctly.
"""
print("\nQ 7.")

age = 23
hasMoney = True

# Uncomment this code
if age >= 19:
	print("You are old enough")
	if hasMoney == True:
		print("You can buy alcohol")
	else:
		print("You cannot buy alcohol")
else:
	print("You are not old enough to buy alcohol")



"""
	8.) This question is similar to question 6 however this time
	you are dealing with an Am and PM clock time. The variable
	amPmTime contains the value in a string "4pm"
	
	Print the following based on the value of currentHour
	12am to 12pm inclusive = "Morning time"
	1pm to 4pm inclusive = "Afternoon time"
	5pm to 8pm inclusive = "Evening time"
	9pm to 11pm inclusive = "Night time"

	Change the amPmTime value to make sure all of your code
	is correct
"""
print("\nQ 8.")

# amPmTime = "4pm"

amPmTime = input("Please input time in this format hour:am or hour:pm : ")

amOrPm = amPmTime[-2:]
num = amPmTime.replace(amOrPm, "")

num = int(num)

if amOrPm == "am" or amPmTime == "12pm":
	print("Good Morning")
elif num >= 1 and num <= 4:
	print("Afternoon Time")
elif num >= 5 and num <= 8:
	print("Evening Time")
elif num >= 9 and num <= 11:
	print("Night Time")
else:
	print("Mistake")