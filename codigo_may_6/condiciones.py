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

if not (ini <= num <= fin):
    print("Fuera del intervalo")
else:
    print(f"{num} cumple el intervalo")

sem = "rojo"
if sem == "rojo":
    print("parar")

elif sem == "ambar":
    print("precaución")

else:
    print("pasar")

print("parar" if sem == "rojo" else \
       "precaución" if sem=="ambar" else "pasar")

# A if cond else B

# Imprimir si un número es par o impar
numero = 22
if numero % 2 == 0:
    print("par")
else:
    print("impar")

print("par" if numero % 2 == 0 else "impar")

n1 = 10
n2 = 5
menor = n1 if n1 < n2 else n2
