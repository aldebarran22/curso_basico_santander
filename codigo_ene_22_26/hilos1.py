"""
Implementación de hilos en Python
"""
from threading import Thread
from random import randint
from time import sleep


class HiloMensajes(Thread):
    def __init__(self, n=10):
        Thread.__init__(self, name="Mensajes")
        self.n = n

    def run(self):
        pass


class HiloRandom(Thread):
    def __init__(self, ini=1, fin=10):
        Thread.__init__(self, name="Random")
        self.fin = fin
        self.ini = ini

    def run(self):
        pass
