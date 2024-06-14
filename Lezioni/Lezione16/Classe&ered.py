"""class Veicolo:

    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo (self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    

class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero porte: {self.numero_porte}")

class Moto(Veicolo):

    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()"""


"""class Specie:

    def __init__(self, nome, popolazione_iniziale, tasso_di_crescita):
        self.nome = nome
        self.popolazione_iniziale = popolazione_iniziale
        self.tasso_di_crescita = tasso_di_crescita
    
    def cresci(self):
        popolazione_nuova = self.popolazione_iniziale * (1 + (self.popolazione_iniziale/100))
        print (f"La nuova popolazione è {popolazione_nuova}")
    
    def anni_per_superare(self, altra_specie: "Specie"):"""