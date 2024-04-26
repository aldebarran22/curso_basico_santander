"""
Hilos en Python. Heredar de la clase Thread
Poner en marcha varios hilos y esperar a que terminen
Listas con hilos
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
            print(self.name, "n = ", i)
            sleep(randint(1,3))

        print('Termina', self.name)


if __name__=='__main__':
    L = []
    n = 3

    for i in range(n):
        hilo = Hilo(f"hilo-{i+1}", 5)
        L.append(hilo)
        hilo.start()

    for hilo in L:
        hilo.join()

    print('Termina main!')