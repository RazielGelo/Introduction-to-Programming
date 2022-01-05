print("\nQ1:")
# Create a for loop that loops 10 times and prints the numbers 1 to 10

for num in range(1, 11):
    print(num)

print("\nQ2:")    
# Create a list with three strings inside of it. The strings are "apple" "banana" and "orange". Print the second item in the list.

fruits = ["Apple", "Banana", "Orange"]
print(fruits[1])

print("\nQ3:")
# Create a boolean variable and set it to True. Write an if else statement checking the variable. If it is True, print "Hello World". If it is False, print "Goodbye".

to_greet = True

if to_greet == True:
    print("Hello World")
else:
    print("Goodbye")

print("\nQ4:")
# Create a function that takes a single parameter. Have this function return "Welcome X" where X is the parameter. Call this function and pass your first name in as the parameter.

def greet(name):
    return f"Welcome {name}"

# Only added print for the purpose of printing an output
print(greet("Angelo")) 

colourList  =  [ "red", "green", "blue", "purple", "black", "white" ]	 

for  colour  in  colourList:
	if  colour  ==  "green":
		continue
	elif  colour  ==  "purple":
		break
	print( colour )	
 
print(colourList[0:3:1])
 
num = 0
while num <= 10:
    print(num)
    num +=1

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[2:-2:2])

# Create a function that takes in two parameters that will return their sum. 
def my_sum(para1,para2):
    parasure = int(para1)
    return para1 + para2

print(my_sum(1,2))


class Upper:
    color = "green"
    def __init__(self):
        pass
    def add(self, num1, num2):
        return num1 + num2
    
angelo = Upper()

print(angelo.add(5,5))

my_list = ["A", "B"]
my_list.extend(["C", 0])

print(my_list)

string_name = "Angelo"

string_name.find("A")




    
