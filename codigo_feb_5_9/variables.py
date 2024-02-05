"""
Definir variables, cambiar de tipo.
Utilización de las funciones: int, float y str
int convierte texto a int
float convierte texto a float
str convierte números a texto
"""

# definición de variables:
numero = 100
print(numero, type(numero))

# Leer de teclado:
numero2 = input("Teclear un número:")
print(numero2, type(numero2))

# Solo se pueden sumar tipos compatibles:
# print(numero + numero2)
aux = float(numero2)
print(numero + aux)