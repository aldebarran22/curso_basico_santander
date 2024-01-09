"""
Tuplas en Python, definición, uso, listas de tuplas ...
Con las tuplas podemos parametrizar consultas de SQL:
select * from clientes where pais = ?

Para obtener el resultado de una consulta a la BD:
(10248,'WILMK',5,3,32.38,'Finlandia')
"""
# Definición:
t = (1, 2, 3, 4)
print(t, type(t))

t2 = 5, 6, 7, 8
print(t2, type(t2))

# tuplas de un solo elemento:
t3 = 5  # Mal, es un int entre paréntesis
print(t3, type(t3))

t3 = (5,)
print(t3, type(t3))

# t3[0] = 100 Error, la tupla no se puede modificar.

# Prueba con count:
t = (1, 4, 5, 6, 5, 4, 3, 1, 3, 4, 5, 6, 7)
# Cuantas veces se repite el 5
print("El 5 se repite:", t.count(5))
# Que posición ocupa el primer 5:
print("Posición del 5: ", t.index(5))
