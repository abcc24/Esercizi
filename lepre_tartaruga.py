import random

print ("'BANG !!!!! AND THEY'RE OFF !!!!!'")

percorso = []

#\#1


tartaruga = "T"
lepre = "H"

for x in range(1,71):
    percorso.append('_')
    if tartaruga not in percorso:
        percorso.insert(0,tartaruga)
    if lepre not in percorso:
        percorso.insert(0,lepre)
print(percorso)

def tortoise_step():

    for x in random.randint(range(1,11)):
        if x == [1,2,3,4,5]:
            return 3
        if x == [6,7]:
            return -6
        if x == [8,9,10]:
            return 1

def hare_step():

    for x in random.randint(range(1,11)):
        if x == [1,2]:
            return 0
        if x == [3,4]:
            return 9
        if x == 5:
            return -12
        if x == [6,7,8]:
            return 1
        if x == [9,10]:
            return -2

