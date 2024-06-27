"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("patron:", patron)
    for i in L:
        print(i, True if re.match(patron, i) else False)
    print("-" * 20)


# Ejemplo con el .
patron = ".ython$"
L = ["python", "python99", "jython", "2ython", "*ython", "cithon"]
validar(patron, L)

# Validar DNIs:
patron = ""
L = ["51000456Y", "51000456y", "51000456YZ", "567890988"]
validar(patron, L)
