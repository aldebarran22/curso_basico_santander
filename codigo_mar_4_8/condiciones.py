"""
Condiciones en Python. Comprobar si una variable
se encuentra dentro de un intervalo.
"""

ini = 10
fin = 20
numero = -15
if numero >= ini and numero <= fin:
    print("cumple el intervalo")
else:
    print("NO cumple el intervalo")

if ini <= numero <= fin:
    print("cumple el intervalo")
else:
    print("NO cumple el intervalo")

if numero < ini or numero > fin:
    print("NO cumple el intervalo")
else:
    print("cumple el intervalo")

if not (numero >= ini and numero <= fin):
    print("NO cumple el intervalo")
else:
    print("cumple el intervalo")


# condiciones: 0 es False, "" cadena vacía es False, None es False
n = 0
if n:
    # es distinto de cero?
    print(n)
else:
    print("es cero")

# Operador compacto: A if cond else B
print(n if n else "es cero")
