"""lista = [1,2,3,4]

dizionario = {"pari": [], "dispari": []}

for x in lista:
    if x %2 != 0:
        dizionario["dispari"].append(x)
for y in lista:
    if y %2 == 0:
        dizionario["pari"].append(y)

print(dizionario)"""


numbers = [5,10,20,1]
n = 5

for x in numbers:
    if x <= n:
        numbers.remove(x)
        for x in numbers:
            y = sum(numbers)
print(y)