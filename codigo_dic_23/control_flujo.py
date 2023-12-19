"""
Sintaxis básica, instrucciones de bloque: if / bucles
"""

# if compacto:
numero = 10
print("par" if numero % 2 == 0 else "impar")
"""
if numero % 2 == 0:
    print("par")
else:
    print("impar")
"""

# Bucle while infinito:
"""
while True:
    pass
"""

# Teclear un número múltiplo de 10:
numero2 = 0
while numero2 <= 0 or numero2 % 10 != 0:
    snumero2 = input("numero: ")
    if snumero2.isnumeric():
        numero2 = int(snumero2)
    else:
        print('Solo se admiten multiplos de 10')
print("numero2: ", numero2)
