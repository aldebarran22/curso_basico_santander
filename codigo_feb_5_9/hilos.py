"""
Programación concurrente en Python
"""

from threading import Thread
from random import randint
from time import sleep


class Mensajes(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "mensaje: ", i)
            sleep(randint(1, 3))
        print("Termina: ", self.getName())


class Aleatorio(Thread):

    def __init__(self, n=10):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "número: ", randint(1, 50))
            sleep(randint(2, 3))
        print("Termina: ", self.getName())


if __name__ == "__main__":
    m1 = Mensajes("Hilo1", 12)
    m1.start()  # Va a ejecutar run()

    m2 = Aleatorio()
    m2.start()

    m1.join()  # main espera a que termine el hilo m1
    m2.join()
    print("termina main")
