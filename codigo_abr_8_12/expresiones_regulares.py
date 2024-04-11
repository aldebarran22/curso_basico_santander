"""
Validaciones con expresiones regulares
"""

import re

def validar(patron, L):
    print('Patrón: ', patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print('-'*30)


# Validar DNIs:
patron = ""
L = ["12345678AB","12345678A", "234FF", "509988H","62556445G"]
validar(patron, L)