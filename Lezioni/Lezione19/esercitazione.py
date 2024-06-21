"""string = "   fly me   to   the moon  "
li = list(string.split(" "))
for y in list(li):
    if y == "":
        li.remove(y)

li2 = li[-1]
x = list(li2)
x1 = len(x)
print (x1)"""

digits = [4,3,2,1]

y = digits.pop()

print(digits)

new_x = y+1

print (new_x)

new_digits = digits.append(new_x)
print (digits)