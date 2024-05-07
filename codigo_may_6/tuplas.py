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
