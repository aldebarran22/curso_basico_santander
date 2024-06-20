"""
Expresiones regulares con Python
- match
- search
"""

import re

def validar(patron, L):
    print('Patrón: ', patron)
    for i in L:
        if re.match(patron, i):
            print(i, "True")
        else:
            print(i, "False")
    print('-'*30)


# Validar DNIs:
patron = ""
L = ["12345678AA", "50999777","51234567B","1234"]
validar(patron, L)