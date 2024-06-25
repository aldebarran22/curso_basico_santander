"""
Control de flujo:
- Bucle while
- if compacto
"""

numero = 20
print("par" if numero % 2 == 0 else "impar")

n1 = 12
n2 = 34
menor = n2 if n2 < n1 else n1
print(menor)

"""
# Bucle infinito, se corta con Control + C
while True:
    pass
"""

i = 0
while i < 10:
    print(i)
    i += 1