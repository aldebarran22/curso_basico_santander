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


class Alatorio(Thread):

    def __init__(self):
        pass

    def run(self):
        pass
