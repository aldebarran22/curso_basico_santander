"""
Operadores relacionales en Python y ope. lógicos: and, or, not
"""

# Comprobar si una var. está en un rango:
ini = 10
fin = 50
num = 341
if num >= ini and num <= fin:
    print(f"{num} cumple el intervalo")
else:
    print("Fuera del intervalo")

if ini <= num <= fin:
    print(f"{num} cumple el intervalo")
else:
    print("Fuera del intervalo")