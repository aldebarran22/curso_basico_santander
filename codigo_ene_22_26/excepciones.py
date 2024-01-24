"""
Control de excepciones en Python
"""


def test1():
    # Capturar una excepción concreta
    try:
        L = [1, 3, 4, 5, 6]
        print(L[15])
        print("última línea")
    except IndexError as e:
        print(e)
    #print("fin")
        
def test2():
    # Capturar una excepción concreta pero falla otra excepción distinta
    try:
        L = [1, 3, 4, 5, 6]
        print(100/0)
        print(L[15])
        print("última línea")
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    #test1()
    test2()
