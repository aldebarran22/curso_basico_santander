"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 10
tam_buffer = 5

num_productores = 1
num_consumidores = 1


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            pass

            # Generar un item -> un numero aleatorio

            # Comprobar si hay huecos: sem_huecos

            # Escribir en el buffer en exclusión mutua:
            # Colocar el numero en el buffer
            # Cambiar el indice: ind_p

            # liberar el buffer

            # Avisar de que hay nuevo item: sem_items

            # Retardo:


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            pass

            # Comprobar si un nuevo elemento: sem_items

            #  Leer del buffer en exclusión mutua:
            # Quitar el numero en el buffer
            # Cambiar el indice: ind_c

            # liberar el buffer

            # Avisar de que hay nuevo hueco: sem_huecos

            # Retardo:


class TBuffer:
    def __init__(self):
        self.ind_c = 0
        self.ind_p = 0
        self.buffer = [-1] * tam_buffer
        self.mutex = Lock()
        self.sem_huecos = Semaphore(tam_buffer)
        self.sem_items = Semaphore(0)


if __name__ == "__main__":
    if num_muestras % num_productores != 0 or num_muestras % num_consumidores != 0:
        print("El número tiene que estar equilibrado entre el n. de prod/con")
        exit()

    # Calcular el numero de muestras por productor y consumidor:
    num_muestras_prod = num_muestras // num_productores
    num_muestras_con = num_muestras // num_consumidores

    buf = TBuffer()

    productores = []
    consumidores = []

    for i in range(num_productores):
        p = Productor(buf, num_muestras_prod, f"P-{i+1}")
        productores.append(p)
        p.start()

    for i in range(num_consumidores):
        c = Consumidor(buf, num_muestras_con, f"P-{i+1}")
        consumidores.append(c)
        c.start()

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
