# Python MultiLists


multi_lists = [
	['A', 'B', 'C'],
	['D', 'E', 'F'],
	['G', 'H', 'I', 'J'],
]

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

count = 0

for lis in multi_lists:
	count += len(lis)

print(f"There are {count} items in multi_lists")


"""
	3.) Store the three tuples below in a list to create
	a multi dimensional collection variable. The loop through
	every item in this multidimensional collection and print 
	each one out. You will need to create a nested for loop.
"""
print("\nQ 3.")

tupleA = ('one', 'two', 'three')
tupleB = ('four', 'five', 'six')
tupleC = ('seven', 'eight', 'nine')

my_multi_list = [tupleA, tupleB, tupleC]

# Loop through each tuple in my_multi_list
for tpl in my_multi_list:
	# Loop through each item in each tuple
	for item in tpl:
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

		if dictionary[key] == 'STOP':
			stopOutterLoop = True
			break

		print(key + ' ~~ ' + dictionary[key])

	if stopOutterLoop == True:
		break
else:
	print("This print shows you have gotten to the end")



