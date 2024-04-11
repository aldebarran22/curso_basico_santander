"""
Validaciones con expresiones regulares
"""

import re

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



# Validar DNIs:
patron = ""
L = ["12345678AB","12345678A", "234FF", "509988H","62556445G"]
validar(patron, L)