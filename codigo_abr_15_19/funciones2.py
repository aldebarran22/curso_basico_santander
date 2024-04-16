"""
Parámetros de las funciones:
Parámetros:
- obligatorios (tienen que estar a la izq en la cabecera de la función)
- opcionales
- *args --> una tupla
- **kwargs --> un diccionario
"""


def funcion(ob, op=0, *args, **kwargs):
    print("obligatorio:", ob)
    print("opcional:", op)
    print("args:", args)
    print("kwargs:", kwargs)
    print("-" * 30)


funcion(1)
funcion(1, 2, 3, 4, 5, 6, 7, 8, 9)
funcion(1, 2, 3, 4, 5, 6, 7, 8, 9, x=10, y=20)

################################################################
import matplotlib.pyplot as plt

x = list(range(1, 6))
y = [12, 45, 6, 10, 30]
plt.plot(x, y, color="orange", lw=5.0)
plt.show()
