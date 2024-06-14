from paziente import Paziente
from dottore import Dottore

class Fattura():

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        
        self.patient = patient
        self.doctor = doctor


        if doctor.isAvalidDoctor() == True:
            fatture: int = len(patient)
            salary: int = 0
        else:
            patient = None
            doctor = None
            fatture = None
            salary = None
            print("Non è possibile creare una classe poiché il dottore non è valido")

        self.fatture = fatture
        self.salary = salary
        
    def getSalary(self):