"""
Parámetros por referencia (los mutables)
P. por copia (los inmutables)
"""


def funcion(numero, lista):
    numero += 100
    lista.append(100)


if __name__ == "__main__":
    numero = 1
    L = [1, 2, 3]
    print(f"numero: {numero}, lista: {L}")
    # La lista L pasa por referencia
    funcion(numero, L)
    # La lista L pasa por copia
    # funcion(numero, L.copy())

    print(f"numero: {numero}, lista: {L}")
    print(type(funcion), funcion)

    # print(L(0)) # Error L no es una función
    # print(numero[0]) # Error número no es indexable (no es una colección)
