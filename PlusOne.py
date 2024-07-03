digits = [1,2,3,9]

"""lastN = digits.pop()

lastNu = lastN + 1
        
if lastNu < 10:
    digits.append(lastNu)
    print (digits)

else:
    NUM = [int(x) for x in str(lastNu)]
    digits.extend(NUM)
    print(digits)"""

x = map(int, str(digits))

print(x)
####