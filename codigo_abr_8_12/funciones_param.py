"""
Tipos de parámetros en una función de Python
- obligatorios
- opcionales
- tupla: *args
- diccionario: **kwargs
"""
import matplotlib.pyplot as plt

def funcion(ob, op=100, *args, **kwargs):
    print("Obligatorio: ", ob)
    print("Opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 20)

funcion(1)
funcion(1,2,3,4,5)
d = {"x":10, "y":20}
funcion(1,2, d)
funcion(1,2,**d)
funcion(d)

# Rellenar parámetros opcionales de print
L = list(range(10))
for i in L:
    print(i, end=' ')

y = [12,44,3,11,67]
x = list(range(5))

plt.plot(x, y, c="orange")
plt.show()