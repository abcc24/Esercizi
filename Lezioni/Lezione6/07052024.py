#Exercise 1
#1. Copy the code and print the age of
#bob (using the dot notation)
#2. Create an if-statement that prints
#the name of the oldest of the two
#Persons
#3. Create three other Persons. Make
#a list called people with all 5
#Persons.
#4. Make a loop that finds and prints
#the youngest person’s name





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby = []

    def set_hobby(self, hobby): #nuova funzione, non serve _init_ perchè non è quella iniziale
        self.hobby.append(hobby)

    """def chars(self):
        return self.name, self.age"""
    
    def remove_hobby(self, old_hobby): #rimuove quel determinato attributo
        self.hobby.remove(old_hobby)
    
    def __str__(self): #richiama sempre una stringa
        return f"Lalalala {self.age}"
    
alice = Person("alice W.", 45)
bob = Person("Bob M.", 36)

print (bob.age)

if alice.age > bob.age:
    print (alice.name)
else:
    print (bob.name)

alice.set_hobby("Tennis")

alice.set_hobby("rugby")

alice.remove_hobby("rugby")

print(alice.hobby)

tizi: list = [alice, bob, Person("Roberto E.", 40), Person("Aldo D.", 25), Person("Sara C.", 32)]

print(tizi[0])

"""minage = float ("inf")
index_min_age = 0
for i in range(len(tizi)):
    if tizi[i].age < minage:
        minage = tizi[i].age
        index_min_age = i
print(tizi[index_min_age].name, tizi[index_min_age].age)"""



##########
#Exercise 2 (Folder 9 ex_2.py)
#1. Write a class called Student with the attributes name (str) and
#studyProgram (str)
#2. Create three instances. One for yourself, one for your left neighbour and one
#for our right neighbour.
#3. Add a method printInfo that prints the name and studyProgram of a
#Student. Test your method on the objects!
#4. Modify the code and add age and gender to the attributes. Modify your
#printing methods respectively too.

class Student:

    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        return f"Nome {self.name}, studyProgram {self.studyProgram}, age: {self.age}, gender: {self.gender}"

Filippo = Student("Filippo G.", "Python", 21, "male")
Alberto = Student("Alberto B.", "Java", 32, "male")
Christian = Student("Christian", "C++", 29, "male")


print(Filippo.printInfo())

######################################################
"""Exercise 3 (Folder 9 ex_3.py)
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal"""


class Animal:
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs
    
    def getLegs(self):
        return self.legs
    
    def setLegs(self, new_legs):
        self.legs = new_legs

Cane = Animal("Dull", 4)
print(Cane.getLegs())
Cane.setLegs(5)
print(Cane.getLegs())