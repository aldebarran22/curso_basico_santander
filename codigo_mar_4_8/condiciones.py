"""
Condiciones en Python. Comprobar si una variable
se encuentra dentro de un intervalo.
"""

ini = 10
fin = 20
numero = 25
if numero >= ini and numero <= fin:
    print("cumple el intervalo")
else:
    print("NO cumple el intervalo")

if ini <= numero <= fin:
    print("cumple el intervalo")
else:
    print("NO cumple el intervalo")