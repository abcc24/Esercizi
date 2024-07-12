from abc import ABC
from abc import abstractmethod

class CodificatoreMessaggio (ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str):
        self.testoInChiaro = testoInChiaro
    
class DecodificatoreMessaggio (ABC):
    @abstractmethod
    def decodifica (self, testoCodificato):
        self.testoCodificato = testoCodificato


class CifratoreAScorrimento (CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
        super().__init__()
    
    def codifica (self, testoInChiaro):
        dizionario: dict = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i",
                            10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q",
                            18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
        
        parola = ""
        
        for x in testoInChiaro:
            for k, v in dizionario.items():
                if x == v:
                    n = k + self.chiave
                    if n > 26:
                        c = n - 26
                        parola += dizionario[c]
                    else:
                        parola += dizionario[n]
        return parola

class CifratoreACombinazione (CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int) -> None:
        self.n = n
        super().__init__()

    def codifica(self, testoInChiaro: str):
        
        for x in testoInChiaro

numero: CifratoreAScorrimento = CifratoreAScorrimento(4)
print(numero.codifica("gennaro"))