"""
Threads en Python. Heredamos de la clase Thread
2 hilos:
    1) Imprimir n mensajes
    2) Genera números aleatorios
"""

from threading import Thread
from random import randint
from time import sleep


class Mensajes(Thread):
    def __init__(self, n=10, nombre="mensajes"):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " mensaje: ", (i + 1))
            sleep(randint(1, 2))
        print("Termina:", self.getName())


if __name__ == "__main__":
    m1 = Mensajes(12, "mensajero1")
    m2 = Mensajes(9, "mensajero2")

    m1.start()
    m2.start()

    m1.join()
    m2.join()
