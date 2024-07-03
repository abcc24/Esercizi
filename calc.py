#CLASSI ASTRATTE!

from abc import ABC, abstractmethod


class abcAnimal(ABC):

    @abstractmethod
    def verso(self):
        pass


class Cane(abcAnimal):

    def __init__(self, nome: str):
        self.nome: str = nome
    
    def verso (self):
        print("BAU")


class Gatto(abcAnimal):

    def __init__(self, nome: str):
        self.nome: str = nome
    
    def verso (self):
        print("MIAO")


class Coccodrillo(abcAnimal):

    def __init__(self, nome: str):
        self.nome: str = nome
    
    def verso (self):
        print("Come fa?")

from typing import Any

anim: dict [str, Any]= {"key1":"val1",
                        "key2":"val2",
                        "key3":3,
                        "key4":[1,2]}


cane1: Cane = Cane("Fenrir")
cane1.verso()
gatto1: Gatto = Gatto("Bastardo")
gatto1.verso()
coccodrillo1: Coccodrillo = Coccodrillo("Sauron")
coccodrillo1.verso()

lista_animali: list[abcAnimal] = [cane1, gatto1, coccodrillo1]

for a in lista_animali:
    a.verso() #scorrendo questa lista che contiene le instanze delle classi precedenti tutte hanno la funzione verso.
                #poichè verso è una funzione che sta nella classe astratta che è quella principale.
                 #altrimenti da errori di runtime


#@classmethod
#@staticmethod

#assert

i: int = 0
assert i == 0, f"The value must be equal to 0 instead is {i}"

###############################################

import unittest

class Calculations:

    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b
    
    def get_sum(self):
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        return self.a / self.b

    






