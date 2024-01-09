"""
Práctica con listas y funciones
1) Implementar una función que calcula el iva de un producto
A partir de una lista de precios calcular el iva de cada producto
y el resultado se almacena en una nueva lista.
"""


def entre100y150(valor):
    if 100 <= valor <= 150:
        return True
    else:
        return False


def calcularIVA(precio, iva=21):
    resul = round((precio * iva) / 100.0, 2)
    return resul


if __name__ == "__main__":
    precios = [100.6, 230.55, 100, 45.0, 120.3, 55.9]
    ivas = []
    for precio in precios:
        iva = calcularIVA(precio)
        # print(precio, iva)
        ivas.append(iva)
    print(ivas)

    # Lo mismo pero con map: es un iterador
    ivas2 = list(map(calcularIVA, precios))
    print(ivas2)

    # Otro ejemplo:
    nombres = ["Ana", "Marta", "Andrés", "Julio", "Raúl"]
    longitudNombres = list(map(len, nombres))
    print(longitudNombres)

    # Lo mismo que el anterior pero con list comprehension
    longitudNombres2 = [len(i) for i in nombres]
    print(longitudNombres2)

    # Utilizando list compre. calcular el iva de los precios
    # pero con 10%
    ivas3 = [calcularIVA(p, 10) for p in precios]
    print(ivas3)

    # filter:
    precios2 = list(filter(entre100y150, precios))
    print(precios)
    print(precios2)

    # lo mismo con list comprehension:
    precios3 = [p for p in precios if 100 <= p <= 150]
    print(precios3)
    precios3 = [p for p in precios if entre100y150(p)]
    print(precios3)
