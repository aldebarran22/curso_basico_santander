"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print("-" * 20)


if __name__ == "__main__":
    # Cadenas de 3 caracteres:
    patron = r"...$"
    L = ["***", "1234", "abc", "--a", "12345"]
    validar(patron, L)

    # Cadenas de 3 letras mayúsculas/minúsculas:
    patron = r"[A-Za-z][A-Za-z][A-Za-z]$"
    L = ["***", "1234", "abc", "--a", "AAA", "ABCD", "ASe"]
    validar(patron, L)
    exit()

    # Cadenas de 3 números:
    patron = r"[0-9][0-9][0-9]$"
    L = ["***", "1234", "abc", "--a", "AAA", "ABCD", "ASe"]
    validar(patron, L)
