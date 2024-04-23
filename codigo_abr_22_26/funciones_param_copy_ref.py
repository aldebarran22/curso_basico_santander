"""
Prueba de los parámetros en python.
Obj mutables -> por referencia
Obj inmutables -> por valor/copia
"""


def porRef(lista, conjunto, dicc):
    lista.append(100)
    conjunto.add(100)
    dicc[100] = "100"


if __name__ == "__main__":
    L = [1, 2, 3]
    conjunto = {1, 2, 3}
    dicc = {1: "1", 2: "2", 3: "3"}

    porRef(L, conjunto, dicc)

    print("L", L)
    print("conjunto:", conjunto)
    print("dicc:", dicc)
