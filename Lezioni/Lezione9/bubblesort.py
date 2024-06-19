def bubble_sort(x: list[int]):
    for i in range (len(x)):
        for j in range (len(x)-1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp

l: list[int] = [9321, 0, -1, 2831, 12, 3,4,5]
bubble_sort(l)
print(l)