"""
Tipos numéricos: int, float, complex
Funciones de conversión de tipos: int(), float(), complex() y str()
Leer de teclado: input()
"""

# Operar con datos numéricos: int -> float -> complex

resul = 12 + 45.6
print(resul, type(resul))

resul = 12 + 45.6 + 9+4j
print(resul, type(resul))

n1 = int(input('Dame número:'))
n2 = int(input('Dame número:'))
print(n1 + n2)

# Trunca los decimales:
num = int(12.4) # De float a int
print(num)

resul = str(n1) + str(n2)
print(resul, type(resul))

r = resul != ""
print(r, type(r))
