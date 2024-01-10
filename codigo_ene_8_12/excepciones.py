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

    print('fin')


if __name__ == "__main__":
    prueba1()
