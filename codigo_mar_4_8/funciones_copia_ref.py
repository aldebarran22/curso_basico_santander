"""
Parámetros por copia/valor y referencia
"""


def porCopia(cadena, numero, tupla):
    cadena += "mas texto"
    numero *= 2
    tupla += (9, 9, 9)


def porRef(lista, dicc, conjunto):
    lista.append(1000)
    dicc["ZZ"] = 1000
    conjunto.add(1000)


if __name__ == "__main__":
    num = 10
    cad = "hola"
    t = 1, 2, 3
    # Automáticamente se envían copias SON INMUTABLES!
    porCopia(cad, num, t)
    print(cad, num, t)

    L = [1, 2, 3]
    d = {"a": 1, "b": 2, "c": 3}
    c = {1, 2, 3}
    # Se modifican los objetos porque son MUTABLES!
    porRef(L, d, c)
    # Se pueden enviar copia para no modificar los objetos originales
    # porRef(L.copy(), d.copy(), c.copy())
    print(L, d, c)
