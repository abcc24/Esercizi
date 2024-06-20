from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, ID: str):
        super().__init__(first_name, last_name)
        
        self.__ID = ID
    
    def setidCode(self, idCode: str):
        if type(idCode) == str:
            self.__ID = idCode
    
    def getidCode(self):
        return self.__ID
    
    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}, ID: {self.__ID}")
    
paziente1: Paziente = Paziente(first_name="Lollo", last_name="Lallo", ID="r2d2")
paziente2: Paziente = Paziente(first_name="Panco", last_name="Pinco", ID="c3po")

paziente1.patientInfo()
