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
        for i in self.num_muestras:
            numero = randint(1, 30)

            # Comprobar si hay un hueco libre:
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer en exclusión mutua
            with self.buffer.mutex:
                print(self.getName(), "numero:", numero)
                self.buffer.buffer[self.buffer.ind_p] = numero
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer
                print(self.buffer.buffer)

            # Avisar de un nuevo item:
            self.buffer.sem_items.release()

            # Espera:
            sleep(randint(1,4))
            


class Consumidor(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        pass


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

    # Colecciones:
    productores = []
    consumidores = []

    buf = TBuffer()

    # Crear los productores:
    for i in range(num_productores):
        productor = Productor(buf, num_muestras_prod, f"P-{i+1}")
        productor.start()
        productores.append(productor)

    # Crear los consumidores:
    for i in range(num_consumidores):
        consumidor = Consumidor(buf, num_muestras_con, f"C-{i+1}")
        consumidor.start()
        consumidores.append(consumidor)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
