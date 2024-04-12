"""
Crear una lista de hilos y esperar a que terminen
"""

from threading import Thread
from time import sleep
from random import randint

class Mensaje(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name,'mensaje',(i+1))
            sleep(randint(0,2))
        print(self.name,'ha terminado')

if __name__=='__main__':
    hilos = []
    for i in range(4):
        hilo = Mensaje(f'H-{i+1}', randint(5,10))
        hilo.start()
    print('main termina')