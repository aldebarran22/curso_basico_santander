"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""
from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 20
tam_buffer = 10


class Productor(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(num_muestras):
            item = randint(1, 20)
            print("P: ", item)
            # Comprobar si hay hueco:
            self.buffer.sem_huecos.acquire()
            with self.buffer.mutex:
                self.buffer.buffer[self.buffer.ind_p] = item
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer
                print(self.buffer.buffer)

            # Avisar que hay un nuevo item:
            self.buffer.sem_items.release()
            sleep(randint(1, 2))


class Consumidor(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(num_muestras):
            # Comprobar si tiene algún item
            self.buffer.sem_items.acquire()
            with self.buffer.mutex:
                item = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer
                print(self.buffer.buffer)

            # Avisar que hay un nuevo hueco
            self.buffer.sem_huecos.release()
            print("C: ", item)
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
    buf = TBuffer()
    con = Consumidor(buf)
    pro = Productor(buf)

    con.start()
    pro.start()

    con.join()
    pro.join()
