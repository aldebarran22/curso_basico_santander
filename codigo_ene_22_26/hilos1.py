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
        for i in range(self.n):
            print(self.getName(), (i + 1))
            sleep(randint(1, 2))
        print(self.getName(), "termina!")


class HiloRandom(Thread):
    def __init__(self, ini=1, fin=10):
        Thread.__init__(self, name="Random")
        self.fin = fin
        self.ini = ini

    def run(self):
        for i in range(self.ini, self.fin):
            print(self.getName(), randint(self.ini, self.fin))
            sleep(randint(1, 3))
        print(self.getName(), "termina!")


if __name__ == "__main__":
    hm = HiloMensajes()
    hr = HiloRandom(1, 15)

    # Poner en marcha los hilos:
    hm.start()  # Ejecuta el método run
    hr.start()

    # Main espera a que terminen los dos hilos:
    hm.join()
    hr.join()

    # Main espera a que termina
    print("main termina")
