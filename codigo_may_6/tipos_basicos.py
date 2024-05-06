"""
Tipo de las variables.
Operaciones con variables
"""

# Operaciones con variables enteras
numero = 100
print(numero, type(numero))
numero2 = 200
print(numero + numero2)

# Operaciones con variables de texto:
txt1 = "100"
print(txt1, type(txt1))
txt2 = '200'
print(txt1 + txt2)

# print(numero + txt1) Error operación con tipos incompatibles

# Operación con números:
# int: convierte texto a numero.
print(numero + int(txt1))

# str: convierte numeros a texto.
print(str(numero) + txt1)

# Leer de teclado un valor:
# Leer dos números y sumarlos:
num1 = int(input("Teclear un numero:"))
num2 = int(input("Teclear otro numero:"))
print(num1 + num2)






