"""
Crear tuplas
Acceso a los elementos
- NO SE PUEDEN MODIFICAR !!
Operadores: + * in y slicing (funciona igual que en list y str)
 Expansión de tuplas
- count, index

Donde se utilizan:
 - En las consultas a la BD para mostrar los resultados
 - En los parámetros de las funciones. 
 - Intercambio de variables,
 - expansión de tuplas
 - inicializar múltiples : a,b,c = 1,2,3

 select * from clientes where pais=?, ("España",)
"""

t1 = (1, 2, 3, 4, 5)
t2 = 5, 6, 7, 8

print(t1, type(t1))
print(t2, type(t2))

frase = "hola que tal"
t3 = tuple(frase)
print(t3)

print(t3[0])
# t3[0] = 1000 ERROR NO SE PUEDEN MODIFICAR

print((1, 2, 3) + (8, 9))

# Representar en Python una ruta grabada con un GPS.
L = [(40.2, -3.76), (35.8, -15.9), (40.5, -3.55)]
print("Número de coordenas:", len(L))
for i in L:
    print(i[0], i[1])

L = [(40.2, -3.76, 660), (35.8, -15.9, 550), (40.5, -3.55, 600)]
for lat, lon, alt in L:
    print(lat, lon, alt)

# Calcular la altitud media de todas las coordenadas:
total = 0
for t in L:
    total += t[2]
print("La media:", round(total / len(L),2))

# index:

