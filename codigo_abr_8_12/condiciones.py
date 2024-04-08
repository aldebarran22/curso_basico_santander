"""
Condiciones en Python. Comprobar si una var. está o no dentro de un 
intervalo.
"""

ini = 10
fin = 50
num = 12
if num >= ini and num <= fin:
    print(f'{num} está dentro del intervalo')
else:
    print(' no está en el intervalo')

if  ini <= num <= fin:
    print(f'{num} está dentro del intervalo')
else:
    print(' no está en el intervalo')

if not (ini <= num <= fin):
    print(' no está en el intervalo')
else:
    print(f'{num} está dentro del intervalo')

if num < ini or num > fin:
    print(' no está en el intervalo')
else:
    print(f'{num} está dentro del intervalo')

# Comparar dos números, teniendo en cuenta que pueden ser iguales:
n1 = 10
n2 = 20
if n1 < n2:
    print('n1 < n2')

elif n1 > n2:
    print('n1 > n2')

else:
    print("n1 == n2")

# if compacto: A if cond else B

# imprimir si el numero es par o impar:
n = 125
print("par" if n % 2 == 0 else "impar")
menor = n1 if n1 < n2 else n2


