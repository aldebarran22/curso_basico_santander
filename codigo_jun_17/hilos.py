"""
Crear hilos, poner en marcha, listas de hilos
Esperar a que terminen los hilos
"""

from random import randint
from threading import Thread
from time import sleep

class Hilo(Thread):

    def __init__(self, nombre, n):
        Thread.__init__(self, name=nombre)
        self.n = n
        self.lista = []

    def run(self):
        for i in range(self.n):
            numero = randint(1,30)
            self.lista.append(numero)
            print(self.name, "número:", numero)
            sleep(randint(1,3))
            
        print('Termina: ', self.name)