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
            numero = randint(1, 50)
            print(self.getName(), ":", numero)

            # Comprobar si hay hueco:
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer en exc. mutua:
            with self.buffer.mutex:
                # Colocar el número en el buffer:
                self.buffer.buf[self.buffer.ind_p] = numero
                print(self.buffer.buf)
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

            # Avisar que hay un nuevo item:
            self.buffer.sem_items.release()
            sleep(randint(2, 4))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si hay un item:
            self.buffer.sem_items.acquire()

            with self.buffer.mutex:
                numero = self.buffer.buff[self.buffer.ind_c]
                print(self.getName(), ":", numero)
                print(self.buffer.buf)
                self.buffer.buff[self.buffer.ind_c] = -1
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar que hay un hueco:
            self.buffer.sem_huecos.release()
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
    for i in range(num_productores):
        p = Productor(buf, num_muestras_prod, f"P-{i+1}")
        p.start()
        productores.append(p)

    consumidores = []
    for i in range(num_consumidores):
        c = Consumidor(buf, num_muestras_con, f"C-{i+1}")
        c.start()
        consumidores.append(c)

    for i in consumidores:
        i.join()

    for i in productores:
        i.join()
