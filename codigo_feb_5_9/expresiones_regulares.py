"""
Expresiones regulares en Python
"""
import re

def validar(patron, L):
    print('Patrón: ', patron)
    for i in L:
        print(i, re.match(patron, i)!=None)
    print()

# Palabras de 3 letras que terminan en .
patron = "...\.$"
L = ["123","abc","ABC.","....","ab.","abc.qqqq"]
validar(patron, L)