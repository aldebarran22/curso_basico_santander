"""
Expresiones regulares en Python
"""

import re

def comprobarPatron(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, True if re.match(patron, cad) else False)
    print('-' * 20)

# Validar dni
patron = ""
L = ["12345678", "12345678A", "12345678AA"]
comprobarPatron(patron, L)

# Validar hora:

    