"""
Tipos básicos, prueba del tipado dinámico
Definición de variables.
"""

numero = 100
print(numero, type(numero))
numero = 3.5
print(numero, type(numero))
numero2 = "23"
print(numero + int(numero2))

integer1 = 1 
integer2 = 2

suma = integer1 + integer2    # assignment of sum

print ("Sum is", suma)          # print sum

L = [1,3,4]
print(sum(L))
