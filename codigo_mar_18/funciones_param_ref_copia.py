"""
Pasar parámetros mutables e inmutables a funciones
"""


def referencias(L: list, c: set, d: dict) -> None:
    L.append(1000)
    c.add(1000)
    d["a"] = 1000


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    conjunto = {1, 2, 3, 4, 5}
    diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

    referencias(lista, conjunto, diccionario)
    print(lista)
    print(conjunto)
    print(diccionario)
