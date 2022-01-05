# Python
# In-built python Modules
import math
import time
# Our own Modules
import module_example as mycode

print("Hello from Python!")


# Importing in-built Python modules
# print(dir(time))
time.sleep(1)
print(math.pi)

print(mycode.variableString)
print(mycode.variableNumber - 5)
mycode.welcome("James")



# Indenting is important. It shows code blocks
if 10 > 5:
	print("10 is greater than 5")
	print("10 is a big number")

# Python useful commands
print("Outputs to the command line")
name = input("Give me your name?: ")

print("Hello " + name)

# Exception Handling
age = input("What is your age?: ")

try:
	age = int(age)
except:
	age = 0

print(age + 20)

# Variables

if True:
	firstName = "Finn"

print(firstName)

num = 4
decimalNum = 9.9
myBool = True

print(type(num))
print(type(num) is int)
print(type(decimalNum))
print(type(decimalNum) is float)
print(type(myBool))
print(type(myBool) is bool)

myName = str("james")
myAge = int("9")

print(myName + " is " + str(myAge))
print( f"{myName} is {myAge + 10}" )

print(myName.capitalize())
print(myName)

print(dir(math))
