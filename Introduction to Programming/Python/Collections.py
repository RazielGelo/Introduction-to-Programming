# Python Collections
print("WORKING")

#List
# aList = ["A","B","C","D","F"]
# print(aList)
# print(len(aList))
# print(aList[0])
# print(aList[2])
# print(aList[len(aList) - 1])

# print(aList[1:])
# print(aList[:3])
# print(aList[0::2])
# print(aList[1::2])
# print(aList[:])

	



"""
	1.) Below, commented out, are 4 collections. A list, tuple, set and 
	dictionary. They are created with errors. Uncomment the code, fix the 
	errors and print each one along with its type e.g. type(myList).
"""
print("\nQ 1.")


myList = ["list", "tuple", "set", "dictionary"]
myTuple = ("cannot", "change", "a", "tuple")
mySet = {"no", "duplicates", "allowed", "here"}
myDict = {"string": "word", "number": 1, "boolean": True}

print(myList, type(myList))
print(myTuple, type(myTuple))
print(mySet, type(mySet))
print(myDict, type(myDict))



"""
	2.) Below is a list called colours. Add 2 new colours to the list and
	remove the first colour from it. Then print the entire list and after,
	print the the following "There are X colours in my list" where X is
	the number of elements in your list.
"""
print("\nQ 2.")

colours = ["red", "green", "brown", "white"]
colours.extend(["blue","yellow"])
colours.pop(0)

print(colours)
print(f"There are {len(colours)} colours in my new list.")



"""
	3.) Create a tuple called carBrands with 5 strings in it representing
	different car companies. In separate print(), print out:
	- the first element in your tuple
	- the third and fourth element in your tuple
	- the last element in your tuple
	- the first, third and fifth element in your tuple
"""
print("\nQ 3.")

carBrands = ("Ford","Honda", "Toyota", "Audi","Hyundai")
print(carBrands[0])
print(carBrands[2:4])
print(carBrands[-1])
print(carBrands[0::2])




"""
	4.) Create a list and store 3 country names inside it as strings.
	Ask the user using an input to add a new country into the list. If
	the country name doesn't appear in the list, add it in. If it already
	is in the list then insert it in with all the letters capitalized. 
	Print out your list at the end to see the effect,
"""
print("\nQ 4.")

countryList = ["Philippines", "Canada", "Switzerland"]
newCountry = input("Please input a new country into the list: ")
if newCountry not in countryList:
	countryList.append(newCountry)
else:
	countryList.append(newCountry.upper())

print(countryList)

"""
	5.) Below you will find a large list containing numerous numbers. 
	Write code to check and see if the number 13 is present in 
	it. If it is, remove it from the list. Print how many items
	are in this list. Then cast the list to a set to remove any duplicate
	items that may be present. Then print the new number of items in
	the list now that all duplicates have been removed.
"""
print("\nQ 5.")

hugeList = [54, 22, 111, 5, 22, 22, 67, 6, 99, 99, 20, 67, 90,
			123, 110, 4, 18, 19, 111, 77, 6, 54, 81, 80, 13, 38]

print(f"Initial length is {len(hugeList)}")
if 13 in hugeList:
	hugeList.remove(13)

print(f'''
{hugeList}
New length after 13 is removed = {len(hugeList)}''')

hugeList = set(hugeList)
print(f'''
{hugeList}
New length after duplicates are removed = {len(hugeList)}''')



"""
	6.) Remove all duplicates from the names list below and then
	print each name in alphabetical order separated by the following
	characters " -- "
"""
print("\nQ 6.")

names = ["james", "mark", "mary", "paul", "mark", "aaron", "mary", "mark"]

names = set(names)
names = list(names)
names.sort()
print(names)

names = " -- ".join(names)
print(names)





"""
	7.) Create a colletion variable that holds the names of 4 of your
	friends paired with their phone number. Decide between a list,
	tuple, set or dictionary to create this. Then, using one of your 
	friend's names, print their name along side their number
"""
print("\nQ 7.")

myFriends = {"Lester": "0917-lester", "Roland": "0917-roland", "Vic": "0918-vic", "Eunice": "0919-eunice"}
friendKey = list(myFriends.keys())[1] 
friendValue = myFriends["Roland"]
print(f"{friendKey}: {friendValue}")

"""
	8.) Below is a dictionary containing some of the richest people in 
	the world along side their net worth. They are randomly ordered. 
	Write code to print out the following: "X is the richest person with
	$YYY. Z is the poorest person with $WWW" where YYY and WWW is the
	number of dollars they have.
"""
print("\nQ 8.")

worldsRichest = {
	"Bernard Arnault": 196000000000, 
	"Bill Gates": 137900000000, 
	"Elon Musk": 278700000000, 
	"Jeff Bezos": 200500000000,
	"Larry Ellison": 127100000000, 
	"Larry Page": 124700000000
}

# sortedRichest = sorted((value,key) for (key,value) in worldsRichest.items())
# sortedRichest.reverse()

# worldsRichest = dict(sortedRichest)
# print(sortedRichest)

wealth = list(worldsRichest.values())
people = list(worldsRichest.keys())

wealthOrdered = sorted(wealth)

wealthiestValue = wealthOrdered[-1]
poorestValue = wealthOrdered[0]

wealthiestPos = wealth.index(wealthiestValue)
wealthiestPerson = people[wealthiestPos]

poorestPos = wealth.index(poorestValue)
poorestPerson = people[poorestPos]

print(f'''
{wealthiestPerson} is the richest person in the list with ${wealthiestValue}.
{poorestPerson} is the poorest person in the list with ${poorestValue}.
''')



