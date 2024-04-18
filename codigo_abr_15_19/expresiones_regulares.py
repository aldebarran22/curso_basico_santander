"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print("-" * 30)


# Validar DNI:
patron = ""
L = ["12345678", "12345678A", "12345678AA", "12B", "1A", ""]
validar(patron, L)
