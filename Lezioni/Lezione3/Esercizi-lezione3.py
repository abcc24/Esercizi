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
