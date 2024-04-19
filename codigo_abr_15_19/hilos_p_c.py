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

            # Generar un nuevo item:
            numero = randint(1, 40)

            # Comprobar si hay hueco: sem_huecos
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer en exclusión mutua
            with self.buffer.mutex:
                print(self.name, "coloca numero: ", numero)

                # Colocar el número en el buffer:
                self.buffer.buffer[self.buffer.ind_p] = numero

                # Modificar el indice:
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

                # Imprimir el buffer:
                print(self.buffer.buffer)

            # Avisar de que hay un nuevo item: sem_items
            self.buffer.sem_items.release()

            sleep(randint(2, 4))

        print("Fin del productor: ", self.name)


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si hay un item:
            self.buffer.sem_items.acquire()

            # Modificar el buffer en exclusión mutua
            with self.buffer.mutex:

                # Recuperar el numero del buffer:
                numero = self.buffer.buffer[self.buffer.ind_c]
                print(self.name, "quita numero: ", numero)

                # Vaciar la casilla que apunta ind_c:
                self.buffer.buffer[self.buffer.ind_c] = -1
                print(self.buffer.buffer)

                # Actualizar el indice:
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar del nuevo hueco:
            self.buffer.sem_huecos.release()

            # Consume el item:
            print(self.name, "consume numero: ", numero)

            sleep(randint(3, 5))

        print("Fin del consumidor: ", self.name)


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
        prod = Productor(buf, num_muestras_prod, f"P-{i+1}")
        prod.start()
        productores.append(prod)

    for i in range(num_consumidores):
        con = Consumidor(buf, num_muestras_con, f"C{i+1}")
        con.start()
        consumidores.append(con)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
