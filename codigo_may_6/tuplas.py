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

t1 = (1,2,3,4)
t2 = 5,6,7,8
print(t1, type(t1))
print(t2, type(t2))

gps = [(40.4, -3.65), (40.41, -3.67), (41.01, -3.77)]
print(len(gps),'coordenadas')
for i in gps:
    print('latitud:',i[0])
    print('longitud:',i[1])

for lat, lon in gps:
    print('lat: ', lat,' lon: ', lon)



