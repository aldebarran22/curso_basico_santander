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
# Cuantas veces se repite el 15
print("El 15 se repite:", t.count(15))
# Que posición ocupa el primer 15:
if 15 in t:
    print("Posición del 15: ", t.index(15))
else:
    print('El 15 no está')
