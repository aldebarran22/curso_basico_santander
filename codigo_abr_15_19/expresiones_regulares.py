"""
Expresiones regulares en Python
"""

import re
from string import ascii_uppercase

def validar(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print("-" * 30)


# Validar terminaciones de ython
patron = r".ython$"
L = ["python", "python38", "jython", "ython", "4ython"]
validar(patron, L)


# Validar terminaciones de ython terminando en un punto
patron = r".ython\.$"
L = ["python.", "python.38", "jython.", "ython", "4ython"]
validar(patron, L)

# Validar DNI:
patron = "[0-9]{1,8}[A-Z]$"
L = ["12345678", "12345678A", "12345678b", "12345678AA", "12B", "1A", ""]
validar(patron, L)

# Validar Matrícula europea:

conso = "".join([i for i in ascii_uppercase if i not in "AEIOU"])
patron = f"\d{4}[" + conso + "]{3}$"
L = ["1234", "1234---", "1234GGTS", "DDC1111", "3344WSA", "5566FRt", "1234GGT"]
validar(patron, L)

patron1 = "\d{4}[A-Z]{3}$"
patron2 = "\d{4}[^AEIOU]{3}$"
for mat in L:
    if re.match(patron1, mat) and re.match(patron2, mat):
        print(mat, "True")
    else:
        print(mat, "False")
