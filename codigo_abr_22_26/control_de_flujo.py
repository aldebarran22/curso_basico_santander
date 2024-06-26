"""
if compacto -> A if cond else B
range
while
"""

# Imprimir si un número es par o impar:
numero = 22
if numero % 2 == 0:
    print("par")
else:
    print("impar")

print("par" if numero % 2 == 0 else "impar")

n1 = 10
n2 = 12
if n1 < n2:
    menor = n1
else:
    menor = n2

menor2 = n1 if n1 < n2 else n2

semaforo = "ambar"
print(
    "parar" if semaforo == "rojo" else "pasar" if semaforo == "verde" else "precaucion"
)

# Bucles:
# range(ini, fin-1, salto=1)

# Del 0 al 9
for i in range(10):
    print(i, end=" ")
print()

# Del 1 al 10
for i in range(1, 11):
    print(i, end=" ")
print()

# Del 0 al 100 de 5 en 5
for i in range(0, 101, 5):
    print(i, end=" ")
print()

# 3 intentos: para teclear un múltiplo
for i in range(3):
    importe = int(input("Importe (for 3 intentos): "))
    if importe % 10 != 0:
        print("Teclear múltiplos de 10")
    else:
        break

if importe % 10 == 0:
    print("El importe es válido")

elif i == 2:
    print("Número de intentos consumido ...")

# Bucle infinito: se corta con control+C
"""
while True:
    print("hola")
"""

# Sin número de intentos:
while True:
    importe = int(input("Importe while: "))
    if importe % 10 != 0:
        print("Teclear múltiplos de 10")
    else:
        break

if importe % 10 == 0:
    print("importe correcto")

print("continue:")
i = 0
while i < 10:
    i = i + 1 # i+=1
    if i % 2 == 0:
        continue
    print(i)
