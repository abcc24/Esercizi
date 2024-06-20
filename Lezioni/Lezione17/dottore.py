from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)

        self.__specialization = specialization
        self.__parcel = parcel

        if type(specialization) == str:
            self.__specialization = specialization
        if type(parcel) == float:
            self.__parcel = parcel
        if type(specialization) != str:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa")
        if type(parcel) != float:
            self.__parcel = None
            print("La parcella inserita non è un float")
    
    def setSpecialization(self, specialization):
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa")
    
    def setParcel(self, parcel):
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float")
    
    def getSpecializzation(self):
        return self.__specialization
    def getParcel(self):
        return self.__parcel
    
    def isAvalidDoctor(self):
        if self.getAge() > 30:
            print(f"Il Dottor {self.getName()} {self.getLastName()} è un valido dottore")
            return True
        else:
            print(f"Il Dottor {self.getName()} {self.getLastName()} non è un valido dottore")
            return False
    
    def doctorGreet(self):
        print (self.greet() + f" Sono uno {self.__specialization}")
    

dottore1: Dottore = Dottore(first_name="Mimmo", last_name="Mammo", specialization="Psichiatra", parcel=1000.00)
dottore1.setAge(31)
dottore1.isAvalidDoctor()
dottore1.doctorGreet()
dottore1.setParcel(1500.00)
dottore1.getParcel()