"""
Prueba del tipado en python
"""

numero = 100
print(numero, type(numero))

numero = 100.5
print(numero, type(numero))

numero = "100"
print(numero, type(numero))

numero2 = 20
# print(numero + numero2) # Error tipos incompatibles
if numero2 > 10:
    print('el numero es mayor que 10')

print('fin del programa')


