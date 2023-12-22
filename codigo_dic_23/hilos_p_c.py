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
        pass


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

if __name__ == '__main__':
    buf = TBuffer()
    con = Consumidor(buf)
    pro = Productor(buf)

    con.start()
    pro.start()

    con.join()
    pro.join()
