"""
Paso de parámetros a las funciones:
- por copia: los inmutables: int, float, complex, bool, str, tuple
- por ref: los mutables: list, set, dict
"""


def porCopia(numero, tupla, cadena):
    numero += 10
    tupla += (10, 100, 1000)
    cadena += "1000"


def porReferencia(lista, c, d):
    lista.append(1000)
    lista += [2000]
    c.add(1000)
    d["d"] = 1000


if __name__ == "__main__":
    num = 100
    tupla = 1, 2, 3
    cad = "hola"

    print(num, tupla, cad)
    porCopia(num, tupla, cad)
    print(num, tupla, cad)

    L = [1, 2, 3]
    c = {1, 2, 3}
    d = {"a": 1, "b": 2, "c": 3}
    print(L, c, d)
    porReferencia(L, c, d)
    print(L, c, d)
