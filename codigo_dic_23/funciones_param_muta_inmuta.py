"""
Paso de parámetros a funciones.
Mutables -> pasan por referencia
Inmutables -> pasan por copia
"""


def referencia(lista):
    lista.append(88)


def copia(num):
    num += 100
    print("en copia num:", num)


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    referencia(L)
    print(L)
    num = 0
    copia(num)
    print(num)
