"""
Crear una clase que representa un hilo y lanzar
varias instancias. Los hilos se almacenarán
en una lista. Thread-main espera a que terminen
la tarea.
"""

from threading import Thread
import threading
from time import sleep
from random import randint


class Hilo(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n
        self.lista = []

    def run(self):
        for i in range(self.n):
            numero = randint(1, 25)
            print(self.name, " numero: ", numero)
            self.lista.append(numero)
            sleep(randint(1, 3))

        print(self.name, " ha terminado!")


if __name__ == "__main__":
    L = []
    for i in range(5):
        hilo = Hilo(f"H-{i+1}", randint(3, 6))
        L.append(hilo)
        hilo.start()

    print("Tenemos ", threading.active_count(), "hilos")
    print(threading.enumerate())

    for hilo in L:
        hilo.join()

    print("main termina!")
