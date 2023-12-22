"""
Programación concurrente con dos hilos
hilo1: Escribir un mensaje por pantalla
hilo2: Generar un número aleatorio
"""
from threading import Thread
from time import sleep
from random import randint


class HiloMensajes(Thread):
    def __init__(self, n=10):
        Thread.__init__(self, name="Mensajes")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "mensaje: ", i)
            sleep(1.5)


class HiloAleatorio(Thread):
    def __init__(self, n=15):
        Thread.__init__(self, name="Aleatorio")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), "numero: ", randint(1, 10))
            sleep(0.5)


if __name__ == "__main__":
    hilo1 = HiloMensajes(15)
    hilo2 = HiloAleatorio(12)

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()
    print("main termina")
