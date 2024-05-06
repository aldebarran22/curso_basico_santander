"""
Operadores relacionales en Python y ope. lógicos: and, or, not
"""

# Comprobar si una var. está en un rango:[10,50]
ini = 10
fin = 50
num = 34
if num >= ini and num <= fin:
    print(f"{num} cumple el intervalo")
else:
    print("Fuera del intervalo")

if ini <= num <= fin:
    print(f"{num} cumple el intervalo")
else:
    print("Fuera del intervalo")

if num < ini or num > fin:
    print("Fuera del intervalo")
else:
    print(f"{num} cumple el intervalo")