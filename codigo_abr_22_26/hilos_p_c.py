"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 15
tam_buffer = 5

num_productores = 1
num_consumidores = 3


class Productor(Thread):

    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            # Generar el número aleatorio:
            numero = randint(1,20)
            print(self.name, " PRODUCE: ",numero)

            # Comprobar si hay hueco
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer en exclusión mutua: 
            # comprobar el mutex
            with self.buffer.mutex:
                # Escribir el numero en el buffer:
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(self.buffer.buffer, " <<<=== ", numero)

                # Actualizar el indice del productor
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

                # liberar el mutex

            # Avisar que hay un nuevo item:
            self.buffer.sem_items.release()

            # Espera de tiempo con sleep:
            sleep(randint(2,4))


class Consumidor(Thread):

    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            
            # Comprobar si hay algún item en el buffer:
            self.buffer.sem_items.acquire()

            # Recuperar un valor del buffer en exclusión mutua:
            with self.buffer.mutex:
                # Coger el numero y vaciar la casilla:
                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1

                # Actualizar el indice del consumidor:
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

                print(self.buffer.buffer, " ===>>> ", numero)

            # Avisar que hay un nuevo hueco en el buffer:
            self.buffer.sem_huecos.release()

            # Consumir el item:
            print(self.name, " CONSUME: ",numero)

            sleep(randint(2,4))


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
        productor = Productor(buf, num_muestras_prod, f"P-{i+1}")
        productores.append(productor)
        productor.start()

    for i in range(num_consumidores):
        consumidor = Consumidor(buf, num_muestras_con, f"C-{i+1}")
        consumidores.append(consumidor)
        consumidor.start()

    for hilo in productores:
        hilo.join()

    for hilo in consumidores:
        hilo.join()
