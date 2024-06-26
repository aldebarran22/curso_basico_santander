"""
Paso de parámetros mutables (list, set, dict) e 
inmutables (int / float, str, tuple)
"""


def mutables(lista, conjunto, diccionario):
    print(
        "en la funcion: lista: ", id(lista), "c:", id(conjunto), "d:", id(diccionario)
    )
    lista.append(100)
    conjunto.add(100)
    diccionario["x"] = 100


def inmutables(numero, tupla, cadena):
    print("En la funcion n: ", id(numero), "t: ", id(tupla), "cad:", id(cadena))
    numero += 100
    tupla += (100, 200)
    cadena += "adios"


def inmutables2(numero, tupla, cadena):
    numero += 100
    tupla += (100, 200)
    cadena += "adios"
    return numero, tupla, cadena


if __name__ == "__main__":
    L = [1, 2, 3]
    c = {1, 2, 3}
    d = {"a": 1, "b": 2, "c": 3}
    print("L: ", id(L), "c:", id(c), "d:", id(d))
    mutables(L, c, d)
    print(L, c, d)

    n = 1
    t = (1, 2, 3)
    cad = "hola"
    print("n: ", id(n), "t: ", id(t), "cad:", id(cad))
    inmutables(n, t, cad)
    print(n, t, cad)

    # Retornando los inmutables:
    n, t, cad = inmutables2(n, t, cad)
    print(n, t, cad)


    L = [1,2,3]
    print("L: ", id(L))
    L2 = L.copy()
    print("L2: ", id(L2))

    cad = "hola"
    cad2 = cad.upper()
    print('cad: ', id(cad))
    print('cad2: ', id(cad2))
