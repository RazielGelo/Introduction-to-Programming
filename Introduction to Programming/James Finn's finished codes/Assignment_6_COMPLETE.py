# Python Assignment 6

"""
    1.) Updating a CSV file
    You are given a CSV file called exam_results.csv which contains three
    exam results for 4 students each. The first line contains the names
    of the students. The next three lines contain the results. Commas (,)
    separate each piece of data from each other while the new line denotes
    a new row of data. 

    Write a function that takes in this file, adds "Total" and "Average"
    to the top line and then for each of the other lines place the 
    sum/total of all the numbers in that row and beside that place the
    average of the numbers of that row. These values should be floats.
    Make sure to do this in the same file 
    exam_results.csv so that you overwrite the file.

    The function restore_exam_results() is placed underneath to allow you
    to rebuild the file if you make mistakes.

    The original data looks like:
Mark, Bobby, Susan, Mary
60, 77, 96, 81
95, 79, 60, 54
88, 81, 69, 84

    The final data should look like:
Mark, Bobby, Susan, Mary, Total, Average
60, 77, 96, 81, 314.0, 78.5
95, 79, 60, 54, 288.0, 72.0
88, 81, 69, 84, 322.0, 80.5
"""
print("\nQ 1.")

def update_exam_results(file):
    with open(file, mode='r+', encoding='utf-8') as f:
        all_results = f.read()
        results_rows = all_results.split('\n')

        for row in range(len(results_rows)):
            if row == 0:
                results_rows[0] += ', Total, Average'
            else:
                row_nums = [float(i) for i in results_rows[row].split(',')]
                total = sum(row_nums)
                average = total/len(row_nums)
                results_rows[row] += f', {str(total)}, {str(average)}'

        new_results = '\n'.join(results_rows)
        f.seek(0)
        f.write(new_results)

update_exam_results('exam_results.csv')


def restore_exam_results():
    print('exam_results HAS BEEN RESTORED TO ORIGINAL!')
    print('IF YOU DONT WANT THIS TO HAPPEN COMMENT OUT')
    print('restore_exam_results()')
    with open('exam_results.csv', mode='w', encoding='utf-8') as f_restore:
        f_restore.write("""Mark, Bobby, Susan, Mary
60, 77, 96, 81
95, 79, 60, 54
88, 81, 69, 84""")

######################
#restore_exam_results()
######################




"""
	2.) Create a class called GameCharacter. This class should take
    in 3 object attributes.

    name - a string which should be assigned a value by the user at creation
    health - an int which should be fixed to 10
    lives - an int which should be fixed to 3

    The class should have 1 method which is given below called
    describe_character(). This doesn't take in any parameters
    and simply prints out all of the objects attributes and their values.
    Make sure your class has this method

    def describe_character(self):
        print(self.__dict__)

    The class needs 3 other methods which you will need to create:

    take_damage(damage) 
    which takes in a parameter which represents the
    number of damage the character has taken. This will be an int. When
    called the method should print 
    "CharacterName" took X damage" where X is the number of damage.
    Then the damage amount should be removed from the object's health 
    attribute. Then call describe_character() to display the object's 
    current stats and finally the method should check to see if the
    object has any health left. If it has 0 or less health then the
    method should call the lose_life() method.

    lose_life()
    should print
    "CharacterName lost a life" and then decrement the lives attribute
    by 1. Then call describe_character() to display the object's 
    current stats. If the number of lives has reduced to 0 or less,
    print "CharacterName has died!". If not then restore the character's
    health back to it's full value which is 10.

    drink_potion()
    should print
    "CharacterName restored health to full" and then set the health
    attribute to it's original max value of 10. Then call
    describe_character() to display the object's current stats.

    Applying all these together you should have created an object
    representing a videogame character that we can perform actions
    on and track the vital points of information related to the
    character.

    If I was to create a new object from this class and perform 
    the following methods on it like so:

mario = GameCharacter('Mario')

mario.take_damage(4)
mario.take_damage(7)
mario.take_damage(5)
mario.drink_potion()
mario.take_damage(11)
mario.take_damage(15)

    I should see the following output in Command Prompt
Mario took 4 damage.
{'name': 'Mario', 'health': 6, 'lives': 3}
Mario took 7 damage.
{'name': 'Mario', 'health': 0, 'lives': 3}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 2}
Mario took 5 damage.
{'name': 'Mario', 'health': 5, 'lives': 2}
Mario restored health.
{'name': 'Mario', 'health': 10, 'lives': 2}
Mario took 11 damage.
{'name': 'Mario', 'health': 0, 'lives': 2}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 1}
Mario took 15 damage.
{'name': 'Mario', 'health': 0, 'lives': 1}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 0}
This character has died

    Take note that the health value never dips below 0 despite the
    level of damage the character takes. This needs to 
    be programmed into your class. 

    Also take note that if I continue calling methods on the
    object after it has died, that is ok. No need to write code to 
    prevent this
"""

print("\nQ 2.")

class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3

    def take_damage(self, damage):
        print(f'{self.name} took {damage} damage.')
        self.health = max(0, self.health-damage)
        self.describe_character()
        if self.health <= 0:
            self.lose_life()

    def drink_potion(self):
        print(f'{self.name} restored health to full.')
        self.health = 10
        self.describe_character()

    def lose_life(self):
        print(f'{self.name} lost a life.')
        self.lives -= 1
        self.describe_character()
        if self.lives <= 0:
            print('This character has died')
        else:
            self.health = 10

    def describe_character(self):
        print(self.__dict__)


mario = GameCharacter('Mario')


mario.take_damage(4)
mario.take_damage(7)
mario.take_damage(5)
mario.drink_potion()
mario.take_damage(11)
mario.take_damage(15)
