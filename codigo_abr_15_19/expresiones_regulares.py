"""
Expresiones regulares en Python
"""

import re

def validar(patron, L):
    print('Patrón: ', patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print('-'*30)

