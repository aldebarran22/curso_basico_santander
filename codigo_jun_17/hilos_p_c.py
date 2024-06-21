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
            # Generar el item:
            numero = randint(1,20)
            print(self.name, "GENERA",numero)

            # Comprobar si tiene hueco:
            self.buffer.sem_huecos.acquire()

            # Escribir el número en exclusión mutua:
            with self.buffer.mutex:
                
                # Escribir el número en el buffer con el ind_p
                self.buffer.buffer[self.buffer.ind_p] = numero

                # Imprimir la lista del buffer:
                print(self.name, self.buffer.buffer)

                # Actualizar el índice del productor:
                self.buffer.ind_p = (self.buffer.ind_p + 1)  % tam_buffer

            # Avisar que hay un nuevo item:
            self.buffer.sem_items.release()

            sleep(randint(2,4))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si tiene un item para consumir:
            self.buffer.sem_items.acquire()

            with self.buffer.mutex:
                
                # Recuperar un numero del buffer:
                numero = self.buffer.buffer[self.buffer.ind_c]

                # Macar la casilla como libre
                self.buffer.buffer[self.buffer.ind_c] = -1

                # Imprimir la lista del buffer:
                print(self.name, self.buffer.buffer)

                # Actualizar el indice del consumidor:
                self.buffer.ind_c = (self.buffer.ind_c + 1)  % tam_buffer

            # Avisamos de que hay nuevo hueco:
            self.buffer.sem_huecos.release()

            sleep(randint(3,4))


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
        nombre = f"P-{i+1}"
        prod = Productor(buf, num_muestras_prod, nombre)
        prod.start()
        productores.append(prod)

    for i in range(num_consumidores):
        nombre = f"C-{i+1}"
        con = Consumidor(buf, num_muestras_con, nombre)
        con.start()
        consumidores.append(con)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()

