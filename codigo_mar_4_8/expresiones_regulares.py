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
    # DNI:
    patron = ""
    L = ["AWWEE", "51000123", "65000123J"]
    validar(patron, L)
