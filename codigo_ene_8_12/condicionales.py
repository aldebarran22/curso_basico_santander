"""
Condiciones: comprobar si una variable
se encuentra dentro de un intervalo.
"""

numero = 10
ini = 5
fin = 15

# Comprobar si cumple un intervalo:
if numero >= ini and numero <= fin:
    print(numero, "cumple el intervalo")
else:
    print("no lo cumple")

if ini <= numero <= fin:
    print(numero, "cumple el intervalo")
else:
    print("no lo cumple")
