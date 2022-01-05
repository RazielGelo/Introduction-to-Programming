# Python Variables
import math

"""
	1.) Create three string variables called myName, parentName1 
	and parentName2 and assign them values. Then in a single sentence 
	print out "My name is X. My parents' names are Y and Z"
"""
print("\nQ 1.")
myName = "Angelo"
parentName1 = "Malou"
parentName2 = "Louie"
print(f"My name is {myName}. My parents' names are {parentName1} and {parentName2}.")



"""
	2.) Create a string variable called petName and give it a string value. 
	Create an integer and call it petAge and assign it a value. Print the
	sentence "X is my pet and they are Y years old". Make sure to cast the
	petAge variable as a string before outputting the sentence.
"""
print("\nQ 2.")
petName = "Prince"
petAge = 8
print(f"{petName} is my pet and they are {str(petAge)} years old.")



"""
	3.) Four strings are provided below representing files. They have file 
	extensions such as .txt, .html and .js at the end. Print out each file name 
	without the file extension. Only remove the file extension from the end
"""
print("\nQ 3.")
s1 = "homework.txt"
s2 = "assignment2.html"
s3 = "main.js"
s4 = "js.mainjs.js"

print(s1.strip(".txt"))
print(s2.strip(".html"))
print(s3.strip(".js"))
print(s4.replace(".js","")) # or print(s4.rstrip(".js"))



"""
	4.) Four strings are provided below. Update each one of the strings by
	removing all numbers that appear inside them and uppercase the first
	letter. Then in a single sentence print out each new string separated
	by commas e.g. Apple, Orange, Lemon, Tea
"""
print("\nQ 4.")
f1 = "ap12ple"
f2 = "oran454ge"
f3 = "9lem5on5"
f4 = "t12ea"

f1 = f1.replace("12","")
f2 = f2.replace("454", "")
f3 = f3.replace("9","").replace("5","")
f4 = f4.replace("12","")
print(f"{f1}, {f2}, {f3}, {f4}")



"""
	5.) Ask the user to type in their name using input(). Then replace
	all occurences of the letter "a" with "x", and print the following
	"Welcome Nxme! Your name is Y letters long." where Nxme is their 
	inputted converted name and Y is the number of characters in the name. 
	Note that the first letter is capitalized, all subsequent letters are 
	lowercase and all "a"s are replaced with "x".
"""
print("\nQ 5.")
name = input("Please enter your name: ")
name = name.replace("a","x")
name = name.replace("A","x")
name = name.capitalize()
print(f"Welcome {name}! Your name is {len(name)} letters long.")



"""
	6.) Create an integer called age and another called year and assign them 
	the values of your age and the current year. Then print a single
	sentence that says "My age is X and I was born in the year YYYY" where
	YYYY is year - age.
"""
print("\nQ 6.")
age = 35
year = 2021

print(f"My age is {age} and I was born in the year {year - age}")



"""
	7.) Do the exact same as above except this time ask the user to input their
	age and the current year
"""
print("\nQ 7.")
inputAge = input("Please enter your age: ")
inputYear = input("Please input current year: ")

inputAge = int(inputAge)
inputYear = int(inputYear)

print(f"My age is {inputAge} and I was born in the year {str(inputYear - inputAge)}")



"""
	8.) There are two variables below representing a temperature in Celsius
	and one in Fahrenheit. Write code that converts the temperatures to the
	opposite scale and print 2 sentences reading "X degrees Celsius is Y degrees 
	Fahrenheit" and vice versa for the other one.
"""
print("\nQ 8.")
tempFahrenheit = 32
tempCelsius = 25

convCelsius = (tempCelsius * 9/5) + 32
print(f"{tempCelsius} degrees Celsius is {convCelsius} degrees Fahrenheit")

convFahrenheit = (tempFahrenheit - 32) * 5/9
print(f"{tempFahrenheit} degrees Fahrenheit is {convFahrenheit} degrees Celsius")



"""
	9.) Calculate the area of a circle that has a radius of 45.5cm. Use
	the correct and accurate value of a pi. Display this result like 
	"6503.882cm^2". Note the area is rounded to three decimal places
"""
print("\nQ 9.")

radiusCircle = 45.5
areaCircle = round(math.pi * (radiusCircle ** 2), 3)
print(f"{areaCircle} cm^2")