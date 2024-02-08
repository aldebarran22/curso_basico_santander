"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("Patrón: ", patron)
    for i in L:
        print(i, re.match(patron, i) != None)
    print()


# Palabras de 3 letras que terminan en .
patron = r"...\.$"
L = ["123", "abc", "ABC.", "....", "ab.", "abc.qqqq"]
validar(patron, L)

# Palabras de 3 letras minusculas que terminan en _
patron = r"[a-z][a-z][a-z]_$"
L = ["abc-", "abc_", "ABC_", "....", "ab_", "abc_qqqq"]
validar(patron, L)

# Validar DNIs
patron = r""
L = ["123", "12345678", "12345678AB", "12345678a", "1A"]
validar(patron, L)
