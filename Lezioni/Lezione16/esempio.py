reader = open("Esercizi/Lezioni/Lezione16/esempio.txt")
print(reader)

try:
    reader.readline()
    print("Sono nella try")
    raise Exception("Eccezione!")

except Exception:
    print("Sono nella exception")

finally:
    print("Sono nella finally")
    reader.close()


"""with open("Esercizi/Lezioni/Lezione16/esempio.txt", "a") as reader:
    l = [f" Sono Alberto"]
    reader.writelines(l)"""