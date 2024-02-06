"""
Bucles y condiciones:
for -> conocemos el número de iteraciones
while -> depende de una resp del user
if compacto
"""

# Bucle infinito en Python
# while True:
#    pass


# Opción 1:
while True:
    numero = int(input("Dame un multiplo de 10:"))
    if numero % 10 != 0:
        print("Sólo múltiplos de 10")
    else:
        print("ok, múltiplo de 10: ", numero)
        break  # Rompe el bucle

# Opción 2:
print("opcion 2:")
numero = int(input("Dame un multiplo de 10:"))
while numero % 10 != 0:
    print("Sólo múltiplos de 10")
    numero = int(input("Dame un multiplo de 10:"))
print("ok, múltiplo de 10: ", numero)

# Imprimir del 1 al 10:
i = 1
while i <= 10:
    print(i)
    i += 1

# if compacto: A if cond. else B
numero = 23
print("par" if numero % 2 == 0 else "impar")

if numero % 2 == 0:
    print("par")
else:
    print("impar")

n1 = 12
n2 = 21
menor = n1 if n1 < n2 else n2
print(menor)

# break (rompe el bucle) / continue (salta iteraciones)
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # break
    print(i)
