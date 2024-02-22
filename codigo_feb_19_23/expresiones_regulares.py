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

    # Validar un DNIs:
    patron = ""
    L = [""]
    validar(patron, L)
