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
    patron = "..."
    L = ["***", "1234", "abc", "--a", "12345"]
    validar(patron, L)

    # DNI:
    patron = ""
    L = ["AWWEE", "51000123", "65000123J"]
    #validar(patron, L)