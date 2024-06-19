"""
Ordenar colecciones. Cambiar los criterios de ordenación con:
- funciones de python
- funciones lambda
- función def
"""

nombres = ["Jose Miguel", "Ana", "Andrés", "Gema", "Juan", "Eva"]
nombres.sort()
print(nombres)

nombres.sort(key=len, reverse=True)
print(nombres)

tuplas = [(1,2,3,4,5), (80,), (4,5,6,7), (8,55)]
tuplas.sort(key=sum)
print(tuplas)


nombres = [("Jose Miguel",34,1.8), ("Ana",29,1.78), ("Andrés",55,1.9)]
nombres.sort()
print(nombres)
nombres.sort(key=lambda t:t[1])
print(nombres)
nombres.sort(key=lambda t:t[2], reverse=True)
print(nombres)