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
patron = r"[0-9]{1,8}[A-Z]$"
patron = r"\d{1,8}[A-Z]$"
L = ["123", "12345678", "12345678AB", "12345678a", "1A", "40156894Q"]
validar(patron, L)

# Matriculas europeas:
patron = "[0-9]" * 4 + "[BCDFGHJKLMNPQRSTWZ]" * 3
patron = "[0-9]{4}[BCDFGHJKLMNPQRSTWZ]{3}"
L = ["1234", "1234dff", "1234AB", "1234RRT", "12345TRT", "1234tGG"]
validar(patron, L)

"""Comprobar la validez del siguiente código:
Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, 
guión bajo y 6 números que no pueden empezar por 0.
COD_AEE_800959
S/N_UOO_958474"""
patron = "(COD|S/N)_[AEIOU]{3}_[1-9][0-9]{5}$"
L = [
    "COD_AEE_800959",
    "S/N_UOO_958474",
    "S/N_UOO_058474",
    "S/N_UoO_958474",
    "C_UOO_123456",
    "|_UOO_123456",
    "///_UOO_123456",
    "CCC_UOO_123456",
]
validar(patron, L)

# Recuperar el objeto que devuelve match:
patron = "(COD|S/N)_([AEIOU]{3})_([1-9][0-9]{5})$"
cad = "COD_AEE_800959"
obj = re.match(patron, cad)
print(obj)
print(obj.groups())
