"""
Expresiones regulares en Python
"""
import re
import string


def comprobar(patron, L):
    print("Patron:", patron)
    for i in L:
        print(
            i,
            True if re.match(patron, i) else False,
            True if re.search(patron, i) else False,
        )
    print("-" * 15)


# Validar palabras de 3 letras que terminan en .
patron = r"^...\.$"
L = ["abc.", "123.", "adv", "123", "abc.5", "1234.", "*-0."]
comprobar(patron, L)


# Validar DNI
patron = "^[0-9]{1,8}[A-Z]$"
L = ["12345678A", "12", "123B", "12345678AB", "12345678a"]
comprobar(patron, L)

"""
EXPRESIONES REGULARES:
1. Comprobar la validez del siguiente código:
Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, 
guión bajo y 6 números que no pueden empezar por 0.
COD_AEE_800959
S/N_UOO_958474
"""
patron = "^(COD|S/N)_[AEIOU]{3}_[1-9][0-9]{5}$"
L = ["COD_AEE_800959", "S/N_UOO_958474", "AAA_AUI_123456", "COD_AEE_012345"]
comprobar(patron, L)

patron = "^(COD|S/N)_([AEIOU]{3})_([1-9][0-9]{5})$"
obj = re.match(patron, "S/N_UOO_958474")
print(obj.groups())

patron = "^[\x30-\x34]{1,5}$"
L = ["abcde", "01234", "22222", "12"]
comprobar(patron, L)

# Validar matrículas europeas:
consonantes = "".join([i for i in string.ascii_uppercase if i not in "AEIOU"])
patron = "^\d{4}[" + consonantes + "]{3}$"
print(patron)
L = ["1234fGG", "0012", "3344SSR", "12234RRHT", "RRT4567", "1234DDF"]
comprobar(patron, L)
