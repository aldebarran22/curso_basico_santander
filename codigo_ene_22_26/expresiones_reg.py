"""
Expresiones regulares en Python
"""
import re


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
patron = ""
L = ["12345678A", "12", "123B", "12345678AB", "12345678a"]
comprobar(patron, L)
