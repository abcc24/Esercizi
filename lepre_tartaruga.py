import random

print ("'BANG !!!!! AND THEY'RE OFF !!!!!'")

percorso = []

t = 0
l = 0

def tortoise_step(step_tort):

    dado = random.randint(1,10)
    if dado == 0 < 6:
        step_tort += 3
    if dado == 5 < 8:
        step_tort -= 6
    if dado == 7 < 11:
        step_tort += 1
    return step_tort

def hare_step(step_hare):

    dado = random.randint(1,10)
    if dado == 0 < 3:
        step_hare += 0
    if dado == 2 < 5:
        step_hare += 9
    if dado == 5:
        step_hare -= 12
    if dado == 5 < 8:
        step_hare += 1
    if dado == 7 < 11:
        step_hare -= 2
    return step_hare


def vis_percorso (percorso):

    hares = hare_step(step_hare=0)
    torts = tortoise_step(step_tort=0) #utilizza questo metodo per richiamare funzione precedente

    for x in range(1,71):
        percorso.append('_')
    
    for y in range(len(percorso)): #inizializza la T e la H utilizzando la posizione nel percorso
        percorso[t] = "T"
        percorso[l] = "H"
        
        print(percorso)

    if percorso[t] == percorso[l]:
        print ("OUCH") #se si printa nella stessa posizione inizializzata [0], la T diventa invisibile

    #while

vis_percorso(percorso)