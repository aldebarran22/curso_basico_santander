"""
Expresiones regulares en Python
"""

import re

def comprobarPatron(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, True if re.match(patron, cad) else False)
    print('-' * 20)

# Validar dni
patron = "[0-9]{8}[A-Z]$"
L = ["12345678", "12345678A","12345678b", "12345678AA"]
comprobarPatron(patron, L)
exit()

# Pruebas con el .
patron = ".ython$"
L = ["python", "  jython", "*ython", "ython", "pythonnnn"]
comprobarPatron(patron, L)

# Cadenas de 3 caracteres que empiezan y terminan por .  ==> ".123.."
patron = "\....\.$"
L = [".....", "123.", ".acd", ".123.", ".12344.",".123.."]
comprobarPatron(patron, L)


# Validar hora:

    