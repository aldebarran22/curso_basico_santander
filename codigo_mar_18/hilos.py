"""
Hilos en Python
"""

from threading import Thread
from time import sleep
from random import randint


class Hilo(Thread):

    def __init__(self, nombre="", n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "i=", i)
            sleep(randint(0, 2))
        print(f"{self.getName()} ha terminado!")


if __name__ == "__main__":
    L = []
    for i in range(4):
        hilo = Hilo(f"Hilo-{i+1}", randint(5, 10))
        hilo.start()
        L.append(hilo)

    for i in L:
        i.join()

    print("main termina")
