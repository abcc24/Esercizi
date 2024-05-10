#Scrivi una funzione che, 
#dato un insieme e una lista di numeri interi da rimuovere, 
#ritorni un nuovo insieme senza i numeri specificati nella lista.



def frequency_dict(elements: list) -> dict:
    # cancella pass e scrivi il tuo codice
    key = elements[0::2]
    values = elements [1::2]
    frequency_dict = {key[x]: values[x] for x in range(len(key))}
    return frequency_dict
elements = ['mela', 1, 'banana', 2]
print(frequency_dict(elements))


################

def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    risultato = {}

    for st in voti:
        name = st["name"]
        voto = st["voto"]

        if name in risultato:
            risultato[name].append(voto)
        else:
            risultato[name] = [voto]
    return risultato
print(aggrega_voti ([{'name': 'Mario', 'voto': 7}, {'name': 'Sara', 'voto': 8}, {'name': 'Mario', 'voto': 6}]))
