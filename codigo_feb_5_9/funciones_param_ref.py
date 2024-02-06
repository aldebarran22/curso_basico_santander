"""
Paso de parámetros a las funciones, por copia
y referencia.
Parámetros inmutables NO se modifican (por copia)
Parámetros mutables SI se modifican (por referencia)
"""


def incrementar(numero):
    numero += 1
    print("en incrementar, numero: ", numero)


if __name__ == "__main__":
    num = 100
    incrementar(num)  # manda una copia!
    print("num:", num)
