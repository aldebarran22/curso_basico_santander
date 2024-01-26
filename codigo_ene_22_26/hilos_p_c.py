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
            # Generar el item:
            numero = randint(1, 10)
            # Comprobar si tiene hueco:
            self.buffer.sem_huecos.acquire()

            # modificar el buffer en exclusión mutua:
            with self.buffer.mutex:
                print(self.getName(), numero)
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(self.buffer.buffer)
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

            # Avisar de que ya tiene un item
            self.buffer.sem_items.release()
            sleep(randint(2, 4))


class Consumidor(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(num_muestras):
            # Comprobar si tiene un item:
            self.buffer.sem_items.acquire()

            with self.buffer.mutex:
                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                print("C: ", numero)
                print(self.buffer.buffer)
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar que hay un nuevo hueco:
            self.buffer.sem_huecos.release()

            sleep(randint(1, 3))


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

    con = Consumidor(buf)
    con.start()

    productores = []
    for i in range(num_productores):
        nombre = "P" + str(i + 1)
        pro = Productor(buf, num_muestras_prod, nombre)
        pro.start()
        productores.append(pro)

    con.join()

    for pro in productores:
        pro.join()
