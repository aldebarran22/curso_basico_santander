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

if not (numero >= ini and numero <= fin):
    print("no lo cumple")
else:
    print(numero, "cumple el intervalo")

if numero < ini or numero > fin:
    print("no lo cumple")
else:
    print(numero, "cumple el intervalo")

n1 = 20
n2 = 20
# Calcular el menor de los dos, teniendo en cuenta que pueden ser iguales
if n1 < n2:
    print(f"El menor es {n1}")

elif n1 == n2:
    print("Los números son iguales!")

else:
    print(f"El menor es {n2}")


# if compacto: A if cond else B
# Imprimir si un número es par o impar
numero = 20
print("par" if numero % 2 == 0 else "impar")

if numero % 2 == 0:
    print("par")
else:
    print("impar")
