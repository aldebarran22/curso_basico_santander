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


