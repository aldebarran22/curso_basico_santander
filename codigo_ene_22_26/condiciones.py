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

if num < ini or num > fin:
    print("No está")
else:
    print("dentro del intervalo")

if ini < fin:
    print("el menor", ini)
elif ini == fin:
    print("iguales")
else:
    print("el menor", fin)
