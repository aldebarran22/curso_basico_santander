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


# Validar cadenas de 3 chars que terminan en .
patron = r"...\.$"
L = ["123.", "FRF.","....", "()-.", "123.."]
validar(patron, L)


# Validar cadenas de 3 letras mayúsculas que terminan en .
patron = r"[A-Z][A-Z][A-Z]\.$"  # patron = r"[A-Z]{3}\.$"
L = ["123.", "FRF.","....", "()-.", "123.."]
validar(patron, L)


# Validar DNIs: dígitos de 1 a 8 y una letra mayúscula
patron = "[0-9]{1,8}[A-Z]$"  # patron = "\d{1,8}[A-Z]$"
L = ["12345678AA", "50999777","51234567B","1234"]
validar(patron, L)

# Validar cadenas de 3 vocales:
patron = "[AEIOUaeiou]{3}$"
L = ["aee","aaaa","AWE","qwrr","aeo","iiiU"]
validar(patron, L)

# Validar matrículas europeas:
patron = ""
L = ["1009SDS", "3344", "12345TTG","8080HHY","1234FFE","9909JJU"]
validar(patron, L)
