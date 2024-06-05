class Weapons:

    def __init__(self, nome: str, tipo: str, danni: int, valore: str):
        self.nome = nome
        self.tipo = tipo
        self.danni = danni
        self.valore = valore
    

    def trovare_arma (self):

        for x in lista_armi:
            if x not in lista_armi:
                lista_armi.append(x)
                print (lista_armi)
            else:
                print("Arma già messa")




arma1: Weapons = Weapons ("Spada lunga", "arma da taglio", 5, "ottima")
arma2: Weapons = Weapons ("Ascia bipenne", "arma da taglio", 8, "buona")
arma3: Weapons = Weapons ("Arco corto", "arma a distanza", 3, "scadente")

lista_armi = [arma1, arma2]

lista_armi.trovare_arma(arma3)