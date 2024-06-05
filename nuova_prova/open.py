file = open("nuova_prova/ciao.txt", "a")

file.write("Cipolle caramellate")

file.close()

file = open("nuova_prova/ciao.txt", "a")

file.write(" Mi piace mangiarle")

file.close()

file = open("nuova_prova/ciao.txt", "r")

print(file.read())