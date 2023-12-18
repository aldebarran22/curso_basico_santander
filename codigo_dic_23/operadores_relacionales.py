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
numero = 19
if numero >= ini and numero <= fin:
    print("Cumple el rango")
else:
    print(numero, "no lo cumple")

if ini <= numero <= fin:
    print("Cumple el rango")
else:
    print(numero, "no lo cumple")

if not (ini <= numero <= fin):
    print(numero, "no lo cumple")
else:
    print("Cumple el rango")

if numero < ini or numero > fin:
    print(numero, "no lo cumple")
else:
    print("Cumple el rango")

print("hex: ", hex(numero))
print("bin:", bin(numero))
print("oct:", oct(numero))
# Rotaciones de bits:
# 0xAF: 1010 1111
# >> 2
# 0010 1011 0x2B
# 0xAF: 1010 1111
# << 2
# 1011 1100
