# Python Objects and Classes

"""
	1.) Create a class called Famiy. Create a class attribute,
	one that doesn't use the __ini__ method,
	for mother, father and sibling (make one up if you don't
	one) and assign them names. Then create an object from this
	and in separate prints, print the following:
	"My father's name is X" for each attribute.
"""
print("\nQ 1.")

class Family:
	father = 'Tom'
	mother = 'Martha'
	brother = 'Bob'

myFamily = Family()

print(f"My father's name is {myFamily.father}")
print(f"My mother's name is {myFamily.mother}")
print(f"My brother's name is {myFamily.brother}")


"""
	2.) Using the myFamily object you created in the previous
	question, change the father attribute value to be "Dad", change
	the mother attribute value to be her original name except 
	this time in all capital letters. After doing this print
	the same line as above but noticed how the values have changed
"""
print("\nQ 2.")

myFamily.father = 'Dad'
myFamily.mother = myFamily.mother.upper()

print(f"My father's name is {myFamily.father}")
print(f"My mother's name is {myFamily.mother}")


"""
	3.) Create a class called Pet (even if you don't have one. 
	Create object attributes (ones that are created inside the 
	__init__ function for this class that you will assign
	values to when it is created. These attributes should be
	animal_type "string", number_legs int and sound "string". Create three new pet
	objects and assign different values for each. Then create 3
	prints, one for each pet, and print the following sentence:
	"cat has 4 legs and says Meow"
	"snake has 0 legs and says Hiss" where you can substitute
	your own values in for each pet object
"""
print("\nQ 3.")

class Pet:
	def __init__(self, animal_type, number_legs, sound):
		self.animal_type = animal_type
		self.number_legs = number_legs
		self.sound = sound

cat = Pet('Cat', 4, 'Meow')
snake = Pet('Snake', 0, 'Hiss')
parrot = Pet('Parrot', 2, 'Squack')

print(f'{cat.animal_type} has {cat.number_legs} legs and says {cat.sound}.')
print(f'{snake.animal_type} has {snake.number_legs} legs and says {snake.sound}.')
print(f'{parrot.animal_type} has {parrot.number_legs} legs and says {parrot.sound}.')



"""
	4.) Create a class to create objects representing planets.
	Each planet must have a name (string), radius km (int), and 
	hasMoon (boolean) attribute that are assigned values when created. 
	They also must have a fixed object attribute called galaxy that
	should always be assigned the value of "Milky Way"
	Create a planet object for Earth, Mars
	and Venus, store these in a tuple and then loop through
	this tuple printing the following sentence: "The planet X
	in the F galaxy has a radius of Y km and has/does not have moons"
"""
print("\nQ 4.")

class Planets:
	#galaxy = 'Milky Way'
	def __init__(self, name, radius, hasMoon):
		self.name = name
		self.radius = radius
		self.hasMoon = hasMoon
		self.galaxy = 'Milky Way'

earth = Planets('Earth', 6371, True)
mars = Planets('Mars', 3390, True)
venus = Planets('Venus', 6052, False)

planets = (earth, mars, venus)
# planets = (
# 	Planets('Earth', 6371, True), 
# 	Planets('Mars', 3390, True), 
# 	Planets('Venus', 6052, False)
# )

for p in planets:
	moon_text = 'has' if p.hasMoon else 'does not have'
	print(f'The planet {p.name} in the {p.galaxy} galaxy, has a radius of {p.radius} km and {moon_text} moons')


"""
    5.) Create a class called FavouriteThings that takes in 2
    object attributes called movie and book. Upon creation of
    an object assign these string values. Create a method
    that will RETURN a string stating "My favourite movie is
    X and my favourite book is Y" where X and Y represent the
    movie and book assigned at the objects creation. Call
    this method and print the string. After this use the
    __dict__ attribute on the object to output the objects
    attributes in command prompt as well.
"""
print("\nQ 5.")

class FavouriteThings:
	def __init__(self, movie, book):
		self.movie = movie
		self.book = book

	def my_fav_things(self):
		return f'My favourite movie is {self.movie} and my favourite book is {self.book}.'

james_fav = FavouriteThings('Space Jam', 'Harry Potter')
print(james_fav.my_fav_things())
print(james_fav.__dict__)



"""
    6.) Create a class called Car that takes in a single 
    object attribute called fuel (an int) that is assigned at 
    the creation of the object. Create a method called drive()
    that takes in a parameter called distance. Drive should
    change the value of the object's fuel attribute everytime
    it is called by reducing fuel by twice the distance the 
    distance that is travelled. If my initial fuel value is
    100 and the object drives a distance of 20 then the fuel
    value should be 60 now (100 - (20 * 2)). Create another
    method called fill_petrol() which automatically sets fuel
    to a value of 100. Create an object from this class and
    experiment by calling drive() and fill_petrol() multiple 
    times and between each of these print out the value of
    the object's fuel to see it change on each call. 
"""
print("\nQ 6.")

class Car:
	def __init__(self, fuel):
		self.fuel = fuel

	def drive(self, distance):
		self.fuel -= distance*2

	def fill_petrol(self):
		self.fuel = 100

car = Car(100)

print(car.fuel)
car.drive(10)
print(car.fuel)
car.drive(15)
print(car.fuel)
car.fill_petrol()
print(car.fuel)



"""
	7.) Create a class called House which takes in 2 object
	attributes called length and width at the moment of creation.
	Create a method called area() which RETURNS the area of
	a house object when called, by multiplying the length
	and width of the house together. Test this method out printing
	its value after you have created a House object with your
	own values. Create another method called 
	market_price(price_per_sqft) which takes in a parameter called
	price_per_sqft (a float) representing how much the house
	costs per 1 square foot. Have this function RETURN a value
	showing the entire cost of the house including the dollar
	symbol. For instance a house object that has a length of
	45 and a width of 25 and a price_per_sqft of 500 should 
	return '$562500'. Print out a value like this. After this
	a disaster strikes! A meteor has hit your house and now
	your house object has lost half of its length (its 
	width stayed the same thankfully). Alter the object's length
	as such and print out the new area of the house. Assuming
	house prices haven't changed since the meteor strike
	the price_per_sqft should stay the same however print 
	out the new market_price which should have been impacted.
"""
print("\nQ 7.")

class House:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.width * self.length

	def market_price(self, pricePerSqFt):
		return f'${self.area() * pricePerSqFt}'

my_house = House(45, 25)

print(my_house.area())
print(my_house.market_price(500))

my_house.length /= 2
print(my_house.area())
print(my_house.market_price(500))
