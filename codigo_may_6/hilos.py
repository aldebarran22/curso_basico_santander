"""
Hilos en Python
Listas de hilos, método join
"""

from threading import Thread
from time import sleep
from random import randint


class Hilo(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, " n = ", i)
            sleep(randint(1, 3))
        print("Termina el hilo: ", self.name)


if __name__ == "__main__":
    L = []
    n = 5
    for i in range(n):
        h = Hilo(f"H-{i+1}", randint(5, 10))
        L.append(h)
        h.start()

    for h in L:
        h.join()
