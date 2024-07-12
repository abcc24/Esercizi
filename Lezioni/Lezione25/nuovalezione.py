from multiprocessing import Process
import time

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

def sleep():

    print(f"Sono nella funzione")
    time.sleep(60)
    print(f"Sto uscendo dalla funzione")

if __name__ =="__main__":
    tic: float = time.time()
    t1 = Process(target=sleep)
    t2 = Process(target=sleep)
    t1.start()
    t2.start()
    toc: float = time.time()
    time_elapsed: float = toc - tic

    print(f"{time_elapsed=}")