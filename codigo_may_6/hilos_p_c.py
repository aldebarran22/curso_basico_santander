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

            # Generar un item -> un numero aleatorio
            numero = randint(1, 10)
            print(f"{self.name} GENERA: {numero}")

            # Comprobar si hay huecos: sem_huecos
            self.buffer.sem_huecos.acquire()

            # Escribir en el buffer en exclusión mutua:
            with self.buffer.mutex:
                # Colocar el numero en el buffer
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(f"{self.name} COLOCA {numero} -> {self.buffer.buffer}")

                # Cambiar el indice: ind_p
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

                # liberar el buffer

            # Avisar de que hay nuevo item: sem_items
            self.buffer.sem_items.release()

            # Retardo:
            sleep(randint(2, 4))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si un nuevo elemento: sem_items
            self.buffer.sem_items.acquire()

            #  Leer del buffer en exclusión mutua:
            with self.buffer.mutex:
                # Quitar el numero del buffer
                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                print(f"{self.name} QUITAR {numero} <- {self.buffer.buffer}")

                # Cambiar el indice: ind_c
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

                # liberar el buffer

            # Avisar de que hay nuevo hueco: sem_huecos
            self.buffer.sem_huecos.release()

            # Consumir el numero:
            print(f"{self.name} CONSUME: {numero}")

            # Retardo:
            sleep(randint(2, 4))


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
