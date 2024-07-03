import random

print ("'BANG !!!!! AND THEY'RE OFF !!!!!!'")

percorso = []

t = 0
l = 0

def tortoise_step():

    dado = random.randint(1,10)
    if dado == 0 < 6:
        return 3
    if dado == 5 < 8:
        return -6
    if dado == 7 < 11:
        return 1

def hare_step():

    dado = random.randint(1,10)
    if dado == 0 < 3:
        return 0
    if dado == 2 < 5:
        return 9
    if dado == 5:
        return -12
    if dado == 5 < 8:
        return 1
    if dado == 7 < 11:
        return -2


def vis_percorso (percorso):

    hares = hare_step()
    torts = tortoise_step() #utilizza questo metodo per richiamare funzione precedente

    for x in range(1,71):
        percorso.append('_')
    
    for y in range(len(percorso)): #inizializza la T e la H utilizzando la posizione nel percorso
        percorso[t] = "T"
        percorso[l] = "H"


    while True:
        if t and l < percorso[70]:
            percorso[l] += hares
            percorso[t] += torts
        if t or l == percorso[70]:
            break
        return percorso[t] and percorso[l]

    if percorso[t] == percorso[l]:
        print ("OUCH") #se si printa nella stessa posizione inizializzata [0], la T diventa invisibile



vis_percorso(percorso)