"""class Person:

    def __init__(self, name, surname, codice_fiscale) -> None:
        self.name = name
        self.surname = surname
        self.codice_fiscale = codice_fiscale
    
    def __eq__(self, value: object) -> bool:
        pass


persona1: Person = Person ("Marco", "Rossi", "df34")
persona2: Person = persona1

persona2.name = "Gabriele"

print(persona1.name)"""


#####

"""Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates).
You may return the answer in any order."""

"""class Solution:
    def CommChar (self, words: list[str]):

        for x in words:
            for y in x:
                if y==y:
                   return y
                

words = ["bella", "zelli", "Ghello"]"""



#######

def fibonacci (i: int):

    a=1
    b=1

    for _ in range(i):

        c=a+b
        a=b
        b=c

    return b
    
print(fibonacci(1000))

######

word = "mississippi"
counter = {}

for letter in word:
     if letter not in counter:
         counter[letter] = 0
     counter[letter] += 1


print(counter)

#####



class ContextManager:

    def __enter__(self):
        print("Risorsa acquisita")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:
            pass

        print ("Risorsa rilasciata")

        return False

with ContextManager() as manager:
    print("Sono dentro with")