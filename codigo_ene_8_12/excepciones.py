"""
Capturar y lanzar excepciones en Python
"""


def prueba1():
    # Capturar un única excepción y tratarla
    try:
        L = [1, 2, 3, 4, 5]
        print("Pos 100:", L[100])
        print("Longitud de L:", len(L))
    except IndexError as e:
        print(e)


def prueba2():
    # Capturar dos excepciones distintas
    try:
        L = [1, 2, 3, 4, 5]
        d = {"a": 1, "b": 2}
        print(d["x"])  # KeyError
        print("Pos 100:", L[100])  # IndexError
        print("Longitud de L:", len(L))
    except IndexError as e:
        print(e)
    except KeyError as e:
        print("No existe la clave del dict: ", e)


if __name__ == "__main__":
    # prueba1()
    prueba2()
