"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore, current_thread
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
        # Generar num_muestras:
        for i in range(self.num_muestras):

            # Generar un item: número aleatorio
            numero = randint(1, 50)
            print(current_thread().name, "PRODUCE:", numero)

            # Comprobar si hay huecos:
            self.buffer.sem_huecos.acquire()

            # Capturar el lock para escribir en el buffer
            # en exclusión mutúa
            with self.buffer.mutex:
                # colocar el número en la casilla
                self.buffer.buffer[self.buffer.ind_p] = numero

                # actualizar el indice del productor
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

                # imprimir el buffer
                print(current_thread().name, self.buffer.buffer)

            # Avisar que ya hay un item al consumidor:
            self.buffer.sem_items.release()

            # Hacer un sleep
            sleep(randint(2, 4))

        print(current_thread().name, " HA TERMINADO")


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        # Generar num_muestras:
        for i in range(self.num_muestras):

            # Comprobar si tiene algún item para consumir
            self.buffer.sem_items.acquire()

            # Capturar el lock para leer del buffer
            # en exclusión mutúa
            with self.buffer.mutex:
                # Recuperar un número del buffer:
                numero = self.buffer.buffer[self.buffer.ind_c]

                # Vaciar la casilla
                self.buffer.buffer[self.buffer.ind_c] = -1

                # Actualizar el indice del consumidor
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar de hay un hueco para el productor
            self.buffer.sem_huecos.release()

            # Consumir el item
            print(current_thread().name, "CONSUME: ", numero)

            # Hacer un sleep
            sleep(randint(2, 5))

    print(current_thread().name, " HA TERMINADO")


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

    # Poner en marcha los productores y los consumidores
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
