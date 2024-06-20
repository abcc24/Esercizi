from paziente import Paziente
from dottore import Dottore

class Fattura():

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        
        self.list_patient = patient
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

        self.salary = self.doctor.getParcel() * len(self.list_patient)
        return self.salary

    def getFatture (self):
        self.fatture = len(self.list_patient)
        return self.fatture

    def addPatient (self, newPatient):
        self.newPatient = newPatient
        if newPatient not in self.list_patient:
            self.list_patient.append(newPatient)
        for newPatient in self.list_patient:
            if newPatient in self.list_patient:
                print (f"Alla lista del dottor {self.doctor.setLastName()}, è stato aggiunto il paziente {newPatient.getidCode()}")

    def removePatient (self,idCode):
        for patient in self.list_patient:
            if patient.getidCode() == idCode:
                self.list_patient.remove(patient)
        print (f"Alla lista del dottor {self.doctor.getLastName} è stato rimosso il paziente {patient.getidCode}")

