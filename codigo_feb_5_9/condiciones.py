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

# Comparar dos número e imprimir: cual es el menor, o el mayor
# o si son iguales:
n1 = 20.5
n2 = 10
if n1 < n2:
    print('El menor es ',n1)

elif n1 > n2:
    print('El menor es ',n2)

else:
    print('son iguales')

nombre1 = "Ana"
nombre2 = "ana"
if nombre1 == nombre2:
    print('El mismo nombre')
elif nombre1 < nombre2:
    print('El menor es:',nombre1)
else:
    print('El menor es ', nombre2)

