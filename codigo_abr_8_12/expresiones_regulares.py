"""
Validaciones con expresiones regulares
"""

import re

def pruebaMatch():
    patron = r"(\d{4})-(\d{4})-(\d{2})-(\d{10})$"
    cc = "   1234-4567-00-1234567890"
    obj = re.search(patron, cc)
    if obj:
        print(obj)
        print(obj.groups())

def validar(patron, L):
    print('Patrón: ', patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print('-'*30)


# Cadenas de 3 minúsculas que terminan en punto:
patron = r"[a-z][a-z][a-z]\.$"
L = ["AEE.","abc.k","123.","abb..","awe.","123 awe."]
validar(patron, L)

# Igual que la anterior, pero con vocales:
patron = r"[aeiou]{3}\.$"
L = ["aaT.","abc.k","123.","abb..","aie.","123 awe."]
validar(patron, L)

# Validar una cuenta bancaria: sucursal-entidad-dc-numero
patron = r"\d{4}-\d{4}-\d{2}-\d{10}$"
L = ["1234-4567-00-1234567890", "1234-4567-001234567890"]
validar(patron, L)


# Validar DNIs:
patron = ""
L = ["12345678AB","12345678A", "234FF", "509988H","62556445G"]
validar(patron, L)

pruebaMatch()

"""
1. Comprobar la validez del siguiente código:
Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, guión bajo y 6 números que no 
pueden empezar por 0.
COD_AEE_800959
S/N_UOO_958474
"""