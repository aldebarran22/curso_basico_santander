"""
Operadores relacionales en Python
== >= <= < > !=
Comprobar si una variable está dentro de un intervalo
"""
ini = 10
fin = 40
num = 15

if num >= ini and num <= fin:
    print("dentro del intervalo")
else:
    print("No está")

if ini <= num <= fin:
    print("dentro del intervalo")
else:
    print("No está")

if not (num >= ini and num <= fin):
    print("No está")
else:
    print("dentro del intervalo")
