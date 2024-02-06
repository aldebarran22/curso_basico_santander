"""
Paso de parámetros a las funciones, por copia
y referencia.
Parámetros inmutables NO se modifican (por copia)
Parámetros mutables SI se modifican (por referencia)
"""


def incrementar(numero):
    numero += 1
    print("en incrementar, numero: ", numero, "id:", id(numero))


def añadir(L):
    L.append(123)
    print(L, id(L))


if __name__ == "__main__":
    num = 100
    print("en main: id: ", id(num))
    incrementar(num)  # manda una copia!
    print("num:", num)

    lista = [1, 2, 3, 4]
    añadir(lista)
    # Si no queremos modificar la lista se puede enviar una copia:
    # añadir(lista.copy())
    print(lista, id(lista))
