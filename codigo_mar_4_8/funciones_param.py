"""
Tipos de parámetros en una función:
- obligatorios
- opcionales
- en una tupla
- en un diccionario
"""
import matplotlib.pyplot as plt

def funcion(ob, op=0, *args, **kwargs):
    print("ob: ", ob)
    print("op: ", op)
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    print()

x = [1,2,3]
y = [1,2,3]
plt.plot(x,y, color="red", lw=3.5, ls='-.')
plt.show()


funcion(100)
funcion(1, 2, 3, 4)
funcion(1, 2, x=3, y=4)
funcion(1, 2, 3, 4, 5, 6, x=300, y=400)

print(1,2,3,4,5,6,7,sep='_')
