#niente implementazione, ovvero lollo = Animale[nome = "Lollo"... e nessun print. verranno messi da loro per fare le prove.
#metti solo i metodi

#metti le funzioni __str__ in ogni classe (credo)

class Zoo:
    def __init__(self, fences, zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    

class Animal:
    def __init__(self, name, species, age, height, width, prefered_habitat, health):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.prefered_habitat = prefered_habitat
        self.health = health


class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat


class ZooKeeper:
    def __init__(self, nome, cognome, matricola):
        self.name = nome
        self.cognome = cognome
        self.matricola = matricola
    
    def add_animal(self, animal: Animal, fence: Fence): #da vedere meglio
        self.animal: Animal = animal
        self.animal.append(animal)
        self.fence: Fence = fence
        self.fence: Fence = fence
    
    def remove_animal(self, animal: Animal, fence: Fence): #da vedere meglio
        self.animal: Animal = animal
        self.animal.remove(animal)
        self.fence: Fence = fence
        self.fence.remove(fence)

    def feed(self, animal: Animal):
        self.animal: Animal = animal

    def clean(self, fence: Fence):
        self.fence: Fence = fence

    def describe_zoo():
        