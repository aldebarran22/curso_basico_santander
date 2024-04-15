"""
Leer variables de teclado y cambios de tipo
Funciones:
int() : Convertir texto a entero int
float() : Convertir texto a float
str() : Convertir a texto
"""

# Leer dos variables y sumarlas:
cad1 = input("Dame número 1: ")
cad2 = input("Dame número 2: ")

if cad1.isnumeric():
    n1 = int(cad1)

if cad2.isnumeric():
    n2 = int(cad2)
    
print(n1 + n2)