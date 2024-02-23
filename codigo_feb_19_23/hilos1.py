"""
Hilos en Python
"""

from threading import Thread
from random import randint
from time import sleep


class HiloRandom(Thread):

    def __init__(self, n=10, name="HiloRandom"):
        Thread.__init__(self, name=name)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(i, self.getName(), randint(1, 50))
            sleep(randint(0, 2))
        print("Fin: ", self.getName())


class HiloMensaje(Thread):

    def __init__(self, n=10, name="HiloMensajes"):
        Thread.__init__(self, name=name)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "mensaje:", i)
            sleep(randint(0, 2))
        print("Fin: ", self.getName())


def test1():
    hiloR = HiloRandom(10)
    hiloM = HiloMensaje(8)

    hiloR.start()
    hiloM.start()

    hiloR.join()
    hiloM.join()

    print("Termina main")


def testLista():
    L = []
    for i in range(5):
        h = HiloRandom(5, f"R-{i}")
        h.start()
        L.append(h)

    for h in L:
        h.join()


if __name__ == "__main__":
    testLista()
