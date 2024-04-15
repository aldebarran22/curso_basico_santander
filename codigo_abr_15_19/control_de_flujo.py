"""
if compacto -> A if cond else B
range
while
"""

# Imprimir si un número es par o impar:
numero = 22
if numero % 2  == 0:
    print('par')
else:
    print('impar')

print("par" if numero % 2 == 0 else "impar")

n1 = 10
n2 = 12
if n1 < n2:
    menor = n1
else:
    menor = n2

menor2 = n1 if n1 < n2 else n2

