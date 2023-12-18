"""
Pruebas con los operadores relacionales en Python
"""
numero1 = 120
numero2 = 450

if numero1 < numero2:
    print(numero1, "es el menor")

elif numero1 == numero2:
    print(numero1, "y", numero2, "son iguales")

else:
    print(numero2, "es el menor")

print("fin de programa")

# Comprobar si un número se encuentra en un rango:
ini = 10
fin = 40
numero = 9
if numero >= ini and numero <= fin:
    print("Cumple el rango")
else:
    print(numero, "no lo cumple")
