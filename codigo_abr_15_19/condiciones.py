"""
Operadores relacionales y lógicos
"""

# Comprobar si una variable se encuentra dentro de un intervalo
ini = 10
fin = 40
num = 0

if num >= ini and num <= fin:
    print(f"El número {num} está dentro del intervalo: {ini},{fin}")
else:
    print('Fuera del intervalo')

if  ini <= num <= fin:
    print(f"El número {num} está dentro del intervalo: {ini},{fin}")
else:
    print('Fuera del intervalo')

if num < ini or num > fin:
    print('Fuera del intervalo')
else:
    print(f"El número {num} está dentro del intervalo: {ini},{fin}")

if not (ini <= num <= fin):
    print('Fuera del intervalo')
else:
    print(f'El número {num} está dentro del intervalo: {ini},{fin}')

nombre1 = "Sara"
nombre2 = 'Sara'

if nombre1 < nombre2:
    print(nombre1, type(nombre1))

elif nombre1 == nombre2:
    print('Es el mismo nombre: ', nombre1)
    
else:
    print(nombre2, type(nombre2))

