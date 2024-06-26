"""
Paso de parámetros mutables (list, set, dict) e 
inmutables (int / float, str, tuple)
"""


def mutables(lista, conjunto, diccionario):
    lista.append(100)
    conjunto.add(100)
    diccionario["x"] = 100


def inmutables(numero, tupla, cadena):
    numero += 100
    tupla += (100, 200)
    cadena += "adios"


if __name__ == "__main__":
    L = [1, 2, 3]
    c = {1, 2, 3}
    d = {"a": 1, "b": 2, "c": 3}

    mutables(L, c, d)
    print(L, c, d)

    n = 1
    t = (1,2,3)
    cad = "hola"
    inmutables(n, t, cad)

    print(n, t, cad)
