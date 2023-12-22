"""
Generar dos hilos con la clase Thread. 
Uno suma 1 a un contador y el otro le resta 1 para un número grande
de iteraciones.
"""
from threading import Thread

contador = 0
iteraciones = 1000000


def sumar():
    global contador
    for i in range(iteraciones):
        contador += 1


def restar():
    global contador
    for i in range(iteraciones):
        contador -= 1


if __name__ == "__main__":
    t1 = Thread(target=sumar)
    t2 = Thread(target=restar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("contador: ", contador)
