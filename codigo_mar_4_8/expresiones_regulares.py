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

    # Cadenas de 3 caracteres y que terminan en punto:
    patron = r"...\.$"
    L = ["abc.", "***.", "1234.", "abc.", "--a.", "12345.", "123"]
    validar(patron, L)

    # DNI:
    patron = r"[0-9]{8}[A-Z]$"
    L = ["AWWEE", "51000123", "65000123J", "12345678AA","12345678b"]
    validar(patron, L)
