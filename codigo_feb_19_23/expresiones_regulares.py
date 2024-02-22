"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        resul = True if re.match(patron, cad) != None else False
        print(cad, " -> ", resul)
    print("-" * 20)


if __name__ == "__main__":
    # Cadenas de 3 caracteres:
    patron = r"...$"
    L = ["abc", "def", "123", "1", "", "1234", "abcd", "---"]
    validar(patron, L)

    # Cadenas de 3 caracteres que terminan en .
    patron = r"...\.$"
    L = ["abc.", "def.", "123", "1.", ".", "1234.", "abcd.", "---."]
    validar(patron, L)

    # Cadenas de 3 caracteres que terminan en \,
    patron = r"...\,$"
    L = ["abc\,", "def,", "123", "1,", ",", "1234,", "abcd,", "---,"]
    validar(patron, L)

    # Validar un DNI:
    patron = "[0-9]{1,8}[A-Z]$"
    L = ["12345678AA", "1B", "234G", "B12345678", "123A56G"]
    validar(patron, L)

    # Objeto match: re.match
    patron = "[0-9]{1,8}[A-Z]$"
    cad = "12345678A"
    obj = re.match(patron, cad)
    print(obj)

    # Objeto match: re.search
    patron = "\d{1,8}[A-Z]$"
    cad = "mi dni es: 12345678A"
    obj = re.search(patron, cad)
    print(obj)

    # Validar una matricula europea: 4 dígitos y 3 consonantes mayúsculas
    patron = "\d{4}[BCDFGHJKLMNPQRSTVWYZ]{3}$"
    L = ["1234AGT", "1234rrt", "4455", "6778HHJ", "1234|||", "6778HHJF"]
    validar(patron, L)

    """
    Comprobar la validez del siguiente código:
    Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, 
    guión bajo y 6 números que no pueden empezar por 0.
    COD_AEE_800959
    S/N_UOO_958474
    """
    patron = "(COD|S/N)_([AEIOU]{3})_([1-9]\d{5})$"
    L = [
        "COD_AEE_800959",
        "S/N_UOO_958474",
        "S/N_UoO_958474",
        "S/N_UOO_95847",
        "COD_AEE_010959",
    ]
    validar(patron, L)

    # Grupos dentro de las expresiones regulares:
    patron = "(COD|S/N)_([AEIOU]{3})_([1-9]\d{5})$"
    cad = "COD_AEE_800959"
    obj = re.match(patron, cad)
    print(obj.groups())
    print("código: ",obj.groups()[2])
