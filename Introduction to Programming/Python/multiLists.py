# Python MultiLists


multi_lists = [
	['Aaa', 'Bb', 'Cccc'],
	['D', 'Eee', 'F'],
	['Gggggg', 'H', 'Iiii', 'J'],
]

print(multi_lists)

"""
	1.) In separate prints, print out the A, D, E, I and J
	from multi_lists. Use the [][] system to access these values.
"""
print("\nQ 1.")

print(multi_lists[0][0])
print(multi_lists[1][0])
print(multi_lists[1][1])
print(multi_lists[2][2])
print(multi_lists[2][3])



"""
	2.) Count the number of items that appear in the entire
	multi_lists. Print the sentence "There are X items 
	in multi_lists"
"""
print("\nQ 2.")

countItems = 0
for i in range(len(multi_lists)):
    for j in range(len(multi_lists[i])):
        countItems += 1
print(countItems)

# OR


count = 0 
countLetters = 0

for inner_list in multi_lists:
    count += len(inner_list)
    for word in inner_list:
        print(word)
        countLetters += len(word)
        
print(countItems)
print(countLetters)

"""
	3.) Store the three tuples below in a list to create
	a multi dimensional collection variable. Then loop through
	every item in this multidimensional collection and print 
	each one out. You will need to create a nested for loop.
"""
print("\nQ 3.")

tupleA = ('one', 'two', 'three')
tupleB = ('four', 'five', 'six')
tupleC = ('seven', 'eight', 'nine')

tupleList = [tupleA, tupleB, tupleC]

for inner in tupleList:
    for item in inner:
        print(item)





"""
	4.) Below is a multi dimensional list containing dictionaries.
	Loop through each one and print both the key and the value
	in each dictionary like so Key ~~ Value. When you encounter the 
	value "STOP"  stop printing anything else from the collection
	and exit out of all the loops
"""
print("\nQ 4.")

multi_dict = [
	{
     	'BC': 'Vancouver',
      	'Ontario': 'Toronto',
       	'Alberta': 'Calgary'
    },
	{
     	'Washington': 'Seattle',
      	'Oregon': 'STOP',
       	'Florida': 'Miami'
    },
	{
     	'UK': 'London',
      	'Ireland': 'Dublin',
       	'France': 'Paris'
    }
 
]

stopOutterLoop = False

# Outter Loop
for dictionary in multi_dict:
    
    # Inner Loop
    for key in dictionary:
        
        if dictionary[key] == "STOP":
            stopOutterLoop = True            
            break
        
        print(key + ' ~~ ' + dictionary[key])
        
    if stopOutterLoop == True:
        break
        
print("This print shows you have gotten to the end.")