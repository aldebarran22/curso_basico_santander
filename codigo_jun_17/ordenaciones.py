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
