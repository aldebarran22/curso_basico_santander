"""
Hilos en Python
"""

from threading import Thread
from time import sleep


class Hilo(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " mensaje: ", i)
            sleep(0.2)
        print("Ha terminado: ", self.getName())


if __name__ == "__main__":
    L = []

    for i in range(3):
        nombre = f"Hilo-{i+1}"
        h = Hilo(nombre)
        h.start()
        L.append(h)

    for h in L:
        h.join()

    print("main terminado")
