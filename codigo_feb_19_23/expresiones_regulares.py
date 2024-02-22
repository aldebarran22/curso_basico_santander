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
    patron = "[0-9]{1,8}[A-Z]$"
    cad = "mi dni  es: 12345678A"
    obj = re.search(patron, cad)
    print(obj)
