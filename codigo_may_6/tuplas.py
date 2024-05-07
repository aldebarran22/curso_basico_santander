"""
Tuplas en Python (son inmutables)
- Crear tuplas
- Operadores: +, *, in
- Slicing
- Expansión de tuplas
- Métodos: index, count
Donde se utilizan tuplas:
- Paso de parámetros a funciones
- Inicialización múltiple de variables
- Intercambiar variables
- SQL: select * from clientes where pais="Francia"
       select * from clientes where pais=? and ingresos > ?, ("Francia", 1000)

- En los resultados de las consultas a la BD.
       nombre, pais, ingresos
       ("aaaa", "bbb", 1200)
       ("12", "ccc", 1300)
"""

t1 = (1, 2, 3, 4)
t2 = 5, 6, 7, 8
print(t1, type(t1))
print(t2, type(t2))

gps = [(40.4, -3.65), (40.41, -3.67), (41.01, -3.77)]
print(len(gps), "coordenadas")
for i in gps:
    print("latitud:", i[0])
    print("longitud:", i[1])

for lat, lon in gps:
    print("lat: ", lat, " lon: ", lon)

# Intercambiar dos variables:
n1 = 10
n2 = 20

n1, n2 = n2, n1
print(n1, n2)

L = [1, 3, 4, 5, 3, 1, 2]
L[0] = 100
t = tuple(L)
print(t)

t = (1, 2, 3)
# t[0] = 10 No se puede modificar la tupla!!

# count e index:
t = (1, 2, 3, 2, 1, 1, 2, 3, 4, 5)
numero = 1
# Obtener todas las posiciones que ocupa el valor de numero:
# 0, 4, 5
