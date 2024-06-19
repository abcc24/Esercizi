import random
import matplotlib

def mergesort (lista_input: list) -> list[int]:

    if len(lista_input)==1:
        return lista_input

    mid_point: int = len(lista_input) // 2 #usato la divisione intera perchè potrebbero esserci liste dispari


    left_list: list[int] = mergesort(lista_input=lista_input[:mid_point])
    right_list: list[int] = mergesort(lista_input=lista_input[mid_point:])

    result: list[int] = merge(right_list, left_list)

    return result

def merge(list1: list[int], list2: list[int]) -> list[int]:

    i, j = 0, 0

    result: list[int] = [None for _ in range(len(list1+list2))]

    for k in range(len(result)):
        if list1[i] > list2[j]:
            result[k] = list2[j]
            j += 1

            if j == len(list2):
                return result[:k+1] + list1[i:]


        else:
            result[k] = list1[i]
            i += 1

            if i == len(list1):
                return result[:k+1] + list2[j:]
            

def bubble_sort(x: list[int]):
    for i in range (len(x)):
        for j in range (len(x)-1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp


import time

if __name__ =="__main__":
    
    list_input: list[int] = [random.randint(0, 10000) for _ in range(10000)]

    start = time.time()
    result: list[int] = mergesort(lista_input=list_input[::-1])
    end = time.time()

    print(f"Mergesort: {end-start}")

    start = time.time()
    result: list[int] = bubble_sort(x=list_input)
    end = time.time()

    print(f"Bubblesort: {end-start}")