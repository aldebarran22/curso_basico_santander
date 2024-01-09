"""
Tuplas en Python, definición, uso, listas de tuplas ...
Con las tuplas podemos parametrizar consultas de SQL:
select * from clientes where pais = ?
"""
# Definición:
t = (1, 2, 3, 4)
print(t, type(t))

t2 = 5, 6, 7, 8
print(t2, type(t2))

# tuplas de un solo elemento:
t3 = (5) # Mal, es un int entre paréntesis
print(t3, type(t3))

t3 = (5,)
print(t3, type(t3))


