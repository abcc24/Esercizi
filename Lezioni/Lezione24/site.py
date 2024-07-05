class Documento:
    def __init__(self, testo: str):
        self.testo = testo

    def getText (self):
        return self.testo
    
    def setText (self, testo: str):
        if type(testo) == str:
            self.testo = testo
    
    def isaTest (self, testo: str):
        if testo == self.testo:
            return True
        
        return False

class Email(Documento):
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo_messaggio = titolo_messaggio

    def getMittente (self):
        return self.mittente
    
    def getDestinatario (self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo_messaggio
    
    def setMittente (self, mittente: str):
        if type(self.mittente) == str:
            self.mittente = mittente

    def setDestinatario (self, destinatario: str):
        if type(self.destinatario) == str:
            self.destinatario = destinatario
    
    def setTitolo (self, titolo_messaggio: str):
        if type(self.titolo_messaggio) == str:
            self.titolo_messaggio = titolo_messaggio
    
    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo()}\nMessaggio: {self.testo}"
    
    def writetoFile (self, percorso: str):
        with open(percorso, "a") as file:
            testo = self.getText()
            file.write(testo)

class File(Documento):
    def __init__(self, nomePercorso: str):
        self.nomePercorso = nomePercorso

        super().__init__(self.leggiTestodaFile())

    def leggiTestodaFile (self):
        with open(self.nomePercorso, "r") as lallo:
            return lallo.read()
        
    def getText (self):
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"
    

x: Email = Email(testo="Ciao Bob, possiamo incontrarci domani?", mittente="alice@example.com", destinatario="bob@example.com", titolo_messaggio="Incontro")
print(x.getText())
y: File = File("Esercizi/Lezioni/Lezione24/document.txt")
print(y.getText())