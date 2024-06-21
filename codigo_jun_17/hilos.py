"""
Crear hilos, poner en marcha, listas de hilos
Esperar a que terminen los hilos
"""

from random import randint
from threading import Thread, enumerate, active_count
from time import sleep

class Hilo(Thread):

    def __init__(self, nombre, n):
        Thread.__init__(self, name=nombre)
        self.n = n
        self.lista = []
        self.on = True    

    def run(self):
        for i in range(self.n):
            if not self.on:
                print('Se va a parar: ', self.name)
                break

            numero = randint(1,30)
            self.lista.append(numero)
            print(self.name, i,"de",self.n, "número:", numero)
            sleep(randint(1,3))

        print('Termina: ', self.name)

    
if __name__=='__main__':
    L = []
    for i in range(5):
        nombre = f"H-{i+1}"
        h = Hilo(nombre, randint(5,10))        
        h.start() # Llama al método run()
        L.append(h)

    print(active_count(),"hilos activos")
    print(list(enumerate()))

    sleep(1)
    L[0].on = False

    for h in L:
        h.join() # Esperar a que termine h!

   

    print('Resultados:')
    for h in L:
        print(h.lista)

    print('termina main')