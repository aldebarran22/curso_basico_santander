"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 10
tam_buffer = 5

num_productores = 2
num_consumidores = 1


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            # Generar un item
            numero = randint(1, 20)
            # Comprobar si tiene un hueco:
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer en exclusión mutua:
            with self.buffer.mutex:
                print(self.getName(), ":", numero)
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(self.buffer.buffer)
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

            # Avisar de que se ha colocado un item:
            self.buffer.sem_item.release()

            sleep(randint(1, 3))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si hay items:
            self.buffer.sem_items.acquire()

            # Quitar un número del buffer en exclusión mutua:
            with self.buffer.mutex:
                numero = self.buffer.buffer[self.buffer.ind_c]
                print(self.getName(), ":", numero)
                self.buffer.buffer[self.buffer.ind_c] = -1
                print(self.buffer.buffer)
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar de que hay un nuevo hueco
            self.buffer.sem_huecos.release()

            # Consumir el dato
            sleep(randint(2, 3))


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

    # Calcular el numero de muestra por productor y consumidor:
    num_muestras_prod = num_muestras // num_productores
    num_muestras_con = num_muestras // num_consumidores

    buf = TBuffer()

    # Crear los hilos:
    LProd = []
    LCon = []

    for i in range(num_productores):
        nombre = f"P-{i+1}"
        p = Productor(buf, num_muestras_prod, nombre)
        p.start()
        LProd.append(p)

    for i in range(num_consumidores):
        nombre = f"C-{i+1}"
        c = Consumidor(buf, num_muestras_con, nombre)
        c.start()
        LCon.append(c)

    for i in LProd:
        i.join()

    for i in LCon:
        i.join()
