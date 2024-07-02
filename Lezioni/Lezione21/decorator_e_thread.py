"""import time

def get_time(func):

    def wrapper(*args):

        start = time.time()

        func(*args)

        end = time.time()
        enlapsed_time = end - start
        print(f"{enlapsed_time=}")
    
    return wrapper

@get_time
def say_hello(name: str) -> None:

    print(f"Hello, {name}")



@get_time
def random_list(upper_bound: int):

    import random
    import time

    sleep_time: int = random.randint(0, upper_bound)
    time.sleep(sleep_time)


@get_time
def say_ciao() -> None:

    print(f"Ciao, Flavio")

say_ciao()

def saluta(func):

    func("Flavio")

saluta(say_hello)
saluta(say_ciao)


def parent():

    print(f"Sono in parent")

    def first_child():

        print(f"Sono in first child")

    def second_child():

        print(f"Sono in second child")

    first_child()
    second_child()

    return second_child

out_function = parent()
print (out_function)
out_function()"""


def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))




def funzione(id: int):
    import time
    import random

    sleep_time: int = random.randint(1,10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":

    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(10))


    #questo qua sotto è l'equivalente di questo qua sopra partendo da "with"
    """lista_thread: list[threading.Thread] = []

    for id in range(3):
    
    
        x: threading.Thread = threading.Thread(target=funzione, args=(id,))
        lista_thread.append(x)
        print(f"Prima di runnare il thread {time.time()}")
        x.start()
        print(f"Ho runnato il thread {time.time()}")

    for t in lista_thread:

        t.join()
        print(f"Terminato!")"""