"""
Operadores relacionales y lógicos en Python
"""

ini = 10
fin = 50
numero = 52

if numero >= ini and numero <= fin:
    print(numero, "dentro del intervalo", ini, fin)
else:
    print("No está en el intervalo")

if ini <= numero <= fin:
    print(numero, "dentro del intervalo", ini, fin)
else:
    print("No está en el intervalo")

if numero < ini or numero > fin:
    print("No está en el intervalo")
else:
    print(numero, "dentro del intervalo", ini, fin)

if not (ini <= numero <= fin):
    print("No está en el intervalo")
else:
    print(numero, "dentro del intervalo", ini, fin)
