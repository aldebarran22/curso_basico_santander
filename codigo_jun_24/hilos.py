"""
Threads en Python
"""

from threading import Thread
from random import randint
from time import sleep


class Hilo(Thread):
    """Genera n números aleatorios"""

    def __init__(self, nombre, n):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " número: ", randint(1, 20))
            sleep(randint(2, 3))
        print("TERMINA: ", self.getName())


if __name__ == "__main__":
    L = []
    n = 5

    for i in range(n):
        hilo = Hilo(f"H-{i+1}", randint(5, 10))
        L.append(hilo)
        hilo.start()

        # hilo.join() OJO, si lo colocamos aquí estamos secuencializando
        # el programa

    for hilo in L:
        hilo.join()

    print("MAIN TERMINA")
