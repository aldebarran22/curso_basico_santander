"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("patron:", patron)
    for i in L:
        print(i, True if re.match(patron, i) else False)
    print("-" * 20)


# Ejemplo con el .
patron = r".ython$"
L = ["python", "python99", "jython", "2ython", "*ython", "cithon"]
validar(patron, L)

# 3 letras vocales que terminen en .
patron = r"[AEIOU]{3}\.$"
L = ["AEE.", "AEI..", "AA.", "aeI.", "UUO"]
validar(patron, L)

# Cadenas que empiezan por 2 digitos, seguidas de un
# tab y terminan en dos letras
patron = r"\d{2}\t[A-Z]{2}$"
L = ["12\tRR", "12 44", "1244", "12     55"]
validar(patron, L)

# Validar DNIs:
patron = "\d{8}[A-Z]$"
L = ["51000456Y", " 51000456y", "51000456YZ", "567890988"]
validar(patron, L)

"""
Comprobar la validez del siguiente código:
Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, 
guión bajo y 6 números que no pueden empezar por 0.
COD_AEE_800959
S/N_UOO_958474
"""
