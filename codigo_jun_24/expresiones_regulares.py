"""
Expresiones regulares en Python
"""

import re

def validar(patron, L):
    print("patron:", patron)
    for i in L:
        print(i, True if re.match(patron, i) else False)
    print('-' * 20)

# Validar DNIs:
patron = ""
L = ["51000456Y", "51000456y", "51000456YZ", "567890988"]
validar(patron, L)

