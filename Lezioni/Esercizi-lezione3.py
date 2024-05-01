#Alberto Baccaro

#Esercizio 4-1
pizze: list=["diavola","marinara","napoli"]
for x in pizze:
    print(x)
"""I made a list of pizzas, the I did a loop to print all the pizzas"""
for x in pizze:
    print(f"I like pizza {x}.")
"""I write a sentence for each type of pizza"""
print(f"I adore the flavour of {x}")

#Esercizio 4-2
animals: list=["Fox", "Wolf", "Dog"]
for x in animals:
    print(x)
"""Like the last exercise I made a loop"""
sentences: list=["is clever", "is strong", "is loyal"]
frase=zip(animals, sentences)
for x, y in frase:
    print(x, y)
print("Those animals are canine")
"""I created another list with sentences and i united with 'zip'. The I made a loop"""

#Esercizio 4-3
for x in range(1,21):
    print(x)
"""I printed numbers from 1 to 20 using range and 'for'"""

#Esercizio 4-4
numbers: list=[index for index in range(1,1000001)]
#for x in range(1,1000001):
    #print(x)
"""I created a list with a range of numbers from 1 to 1000000, then i used a 'for' to print all of them (I used also the step of 1)"""

#Esercizio 4-5
print(min(numbers), max(numbers), sum(numbers))

"""I used max() and min() to see the first and the last number"""

#Esercizio 4-6
num: list=[range(1,21)]
for n in range(1,21):
    if n%2!=0:
       print(n)
"""I created a loop to print odd numbers"""

#Esercizio 4-7
mult: list=[index for index in range(3,33,3)]
print(mult)
"""I created a list using the comprehension list to print all the multiple of 3 (I used the step of 3)"""

#Esercizio 4-8
cube: list=[1,2,3,4,5,6,7,8,9,10]
for c in cube:
    c=c**3
    print(c)
"""I created a list and I used a cicle 'for' to print the cubes of the list"""

#Esercizio 4-9
cube1: list=[i**3 for i in cube]
print(cube1)
"""I used the list comprehention to print the cubes of the list "cube"""

#Esercizio 4-10
listslice=slice(3)
first_three=cube[listslice]
print(first_three)
listslice1=slice(3,6)
middle_three=cube[listslice1]
print(middle_three)
listslice2=slice(7,10)
last_three=cube[listslice2]
print(last_three)
"""I used the list 'cube' of the last exercise.
I used the slice function to take the first three numbers of the list and I created a new list
I did it with the middle numbers and the last numbers"""

#Esercizio 4-11
friends_pizzas: list=["diavola","marinara","napoli"]
pizze.append("margherita")
friends_pizzas.append("montanara")
print("My favorite pizzas are: ")
for x in pizze:
    print(x)
print("My friend's favorite pizzas are: ")
for y in friends_pizzas:
    print(y)

#Esercizio 4-12 (da vedere)

#Esercizio 4-14
#Letto

#Esercizio 4-15 (da aggiornare)
cube: list = [
            1,2,3,4,5,
            6,7,8,9,10
]
for c in cube:
    c = c**3
    print(c)
###

#Esercizio 5-1
car: str = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
"""New tests"""
animal: str = "dog"
print("Is animal == 'dog'? I predict True.")
print(animal == "dog")
print("Is animal == 'beer'? I predict False.")
print(animal == "beer")
###
person: str = "Elisa"
print("Is person == 'Elisa'? I predict True.")
print(person == "Elisa")
print("Is person == 'umbrella'? I predict False.")
print(person == "umbrella")
###
alien: str = "Superman"
print("Is alien == 'Superman'? I predict True.")
print(alien == "Superman")
print("Is car == 'Batman'? I predict False.")
print(alien == "Batman")
###
good_game: str = "Stardew Valley"
print("Is good_game == 'Stardew Valley'? I predict True.")
print(good_game == "Stardew Valley")
print("Is good_game == 'Assassin's Creed Unity'? I predict False.")
print(good_game == "Assassin's Creed Unity")
###
book: str = "The Hobbit"
print("Is book == 'The Hobbit'? I predict True.")
print(book == "The Hobbit")
print("Is book == 'The Hobbit'? I predict False.")
print(book == "Sam")

#Esercizio 5-2
stringa: str = "Hello there!"
print("Is stringa == 'Hello here!'? I predict False.")
print(stringa == "Hello here!")
print("Is stringa != 'I WANT TO FLYYYYYYY!'? I predict True.")
print(stringa != "I WANT TO FLYYYYYYY!")
###
stringa1: str = "Hello"
print("Is stringa1.lower() == 'hello? I predict True")
print(stringa1.lower() == "hello")
print("Is stringa1.lower() == 'Hello'? I predict False")
print(stringa1.lower() == "Hello")
### (It is a bit too long this, so I shorted the boolean answers)
n1: int = 8
n2: int = 3
print(n1 == n2)
#False
print(n1 != n2)
#True
print(n1 > n2)
#True
print(n1 < n2)
#False
print(n1 >= n2)
#True
print(n1 <= n2)
#False
###
a: str = "rana"
b: bool = False
print(a=="rana" and b)
#False
print(a=="rana" or b)
#True
###
names: list = ["Carl", "Anna", "Sam"]
print("Carl" in names)
print("Ron" in names)

#Esercizio 5-3
alien_color: str = "green"
if alien_color is "green":
    print("You earned 5 points")
if alien_color is not "green":
    print("")

#Esercizio 5-4
alien_color: str = "yellow"
if alien_color is "green":
    print("You earned 5 points")
else:
    print("You earned 10 points")
###
alien_color: str = "green"
if alien_color is "green":
    print("You earned 5 points")
else:
    print("You earned 10 points")

#Esercizio 5-5
alien_color: str = "green"
if alien_color is "green":
    print("You earned 5 points")
elif alien_color is "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")
###
alien_color: str = "yellow"
if alien_color is "green":
    print("You earned 5 points")
elif alien_color is "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")
###
alien_color: str = "red"
if alien_color is "green":
    print("You earned 5 points")
elif alien_color is "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")

#Esercizio 5-6
age: int = int(input())
if age< 2:
    print("The person is a baby")
elif 2<= age< 4:
    print("The person is a toddler")
elif 4<= age< 13:
    print("The person is a kid")
elif 13<= age< 20:
    print("The person is a teenager")
elif 20<= age< 65:
    print("The person is an adult")
elif 65<= age:
    print("The person is an elder")

#Esercizio 5-7
favorite_fruits: list = ["orange", "apple", "kiwi"]
if "apple" in favorite_fruits:
    print("You really like apple")
if "orange" in favorite_fruits:
    print("You really like orange")
if "kiwi" in favorite_fruits:
    print("You really like kiwi")
if "banana" in favorite_fruits:
    print("You really like banana")
if "strawberry" in favorite_fruits:
    print("You really like strawberry")

#Esercizio 5-8
username: list = ["admin","admin1","admin2","admin3","admin4"]
for p in username:
    if p == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {p}, thank you for logging in again.")

#Esercizio 5-9
username2: list = []
if not username2:
    print("We need to find some users!")
else:
    for p in username:
        if p == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {p}, thank you for logging in again.")

#Esercizio 5-10
current_users: list = ["Aldo", "Roland", "gianni", "Rebecca", "sandra"]
new_users: list = ["samanta", "Andrea", "Gianni", "AldO", "diego"]
for x in current_users:
    l_user = x.lower()
for new_user in new_users:
    l_new_user = new_user.lower()
    if l_new_user in l_user:
        print(f"The username '{new_user}' is not available.")
        print(f"The username '{new_user}' is available!")

#Esercizio 5-11
numbers = [1,2,3,4,5,6,7,8,9]

for n in numbers:
    if n == 1:
        ord = "1st"
    elif n == 2:
        ord = "2nd"
    else:
        ord = f"{n}th"
    
    print(ord)