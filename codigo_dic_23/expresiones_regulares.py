"""
Expresiones regulares en Python
"""
import re


def testPatron(patron, L):
    d = {palabra: True if re.match(patron, palabra) else False for palabra in L}
    print("Patrón: ", patron)
    for p, r in d.items():
        print(p, "->", r)
    print()


