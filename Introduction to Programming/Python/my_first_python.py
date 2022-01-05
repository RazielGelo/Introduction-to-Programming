# Python
import math    
import time
import module_example
print("Hello from Python!")


# Importing in-built Python Modules
# print(dir(time)) # get directory for modules
# time.sleep(5)
# print(math.pi)

# print(module_example.variableString)
# print(module_example.variableNumber - 5)
# module_example.welcome("Joseph")


# if 10 > 5:
#     print("10 is greater than 5")
#     print("10 is a big number")

# Python useful commands
# print("Outputs to the command line")
# name = input("Give me your name?: ")
# print("Hello " + name) 

#Exception handling
# age = input("How old are you?: ")

# try:
#     age = int(age)
# except: 
#     age = 0

# print(age + 20)


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
print(type(module_example))

myName = str("angelo")
myAge = int("9")

print(myName + " is " + str(myAge))
print(f"{myName} is {myAge}")

print(myName.capitalize())