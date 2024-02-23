"""
Hilos en Python
"""

from threading import Thread
from random import randint
from time import sleep


class HiloRandom(Thread):

    def __init__(self, n=10):
        Thread.__init__(self, name="HiloRandom")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(i, self.getName(), randint(1, 50))
            sleep(randint(0, 2))
        print("Fin: ", self.getName())


class HiloMensaje(Thread):

    def __init__(self, n=10):
        Thread.__init__(self, name="HiloMensajes")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "mensaje:", i)
            sleep(randint(0, 2))
        print("Fin: ", self.getName())


if __name__ == "__main__":
    hiloR = HiloRandom(10)
    hiloM = HiloMensaje(8)

    hiloR.start()
    hiloM.start()

    hiloR.join()
    hiloM.join()

    print("Termina main")
