class Film:

    def __init__(self, titolo: str, durata: int):
        self.titolo = titolo
        self.durata = durata
        ###
    
class Sala:

    def __init__(self, ID: int, film: str, posti_tot: int, posti_pren: int):
        self.ID = ID
        self.film = film
        self.posti_tot = posti_tot
        self.posti_pren = posti_pren

    def prenota_posti(self, num_posti: int):
        if self.posti_tot > num_posti:
            print("Ci sono dei posti disponibili")
        else:
            print("Ci dispiace ma è tutto prenotato")
        

    def posti_disp(self):
        p_disp = self.posti_tot - self.posti_pren
        print(p_disp)
    

class Cinema:

    def __init__(self, lista_sale: list[int], lista_film: list[str]):
        self.lista_sale = lista_sale
        self.lista_film = lista_film

    def aggiungi_sala(self, sala: int):

        if sala in self.lista_sale:
            print("La sala c'è già")
        else:
            self.lista_sale.append(sala)
            print(f"La nuova sala è questa: {sala}")

    def prenota_film(self, titolo_film: str, numero_posti: int):

        a: Sala = Sala

        if titolo_film in self.lista_film:
            if numero_posti > 



film1: Film = Film(titolo = "LOTR", durata = 3)

sala1: Sala = Sala(ID = 4, film = "LOTR", posti_tot = 100, posti_pren = 10)

sala1.prenota_posti(90)
sala1.posti_disp()

cinema1: Cinema = Cinema(lista_sale=[1,2,3,4])

cinema1.aggiungi_sala(5)