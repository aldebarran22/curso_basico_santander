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
            # Generar muestra
            numero = randint(1,20)
            print(self.getName(), ' genera: ',numero)

            # Comprobar si tiene hueco:
            self.buffer.sem_huecos.acquire()

            # Escribir el numero en el buffer en exc. mutua: mutex
            with self.buffer.mutex:
                self.buffer.buffer[self.buffer.ind_p] = numero
                self.buffer.ind_p = (self.buffer.ind_p+1) % tam_buffer
                print(self.buffer.buffer,'-',self.getName(), ' coloca: ',numero)

            # Avisar que hay un nuevo número:
            self.buffer.sem_items.release()

            sleep(randint(2,4))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si hay un item
            self.buffer.sem_items.acquire()

            # Quitar un número del buffer en exc. mutua:
            with self.buffer.mutex:
                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                self.buffer.ind_c = (self.buffer.ind_c+1) % tam_buffer
                print(self.buffer.buffer,'-',self.getName(), ' quita: ',numero)
               

            # Avisar del nuevo hueco
            self.buffer.sem_huecos.release()

            # Consumir el número:
            print(self.getName(), ' consume: ',numero)

            sleep(randint(2,3))



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

    # Crear productores:
    productores = []
    for i in range(num_productores):
        prod = Productor(buf, num_muestras_prod, f"P-{i+1}")
        productores.append(prod)
        prod.start()

    # Crear los consumidores:
    consumidores = []
    for i in range(num_consumidores):
        con = Consumidor(buf, num_muestras_con, f"C-{i+1}")
        consumidores.append(con)
        con.start()

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
