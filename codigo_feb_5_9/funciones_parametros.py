"""
Definir una función con distintos tipos de parámetros
"""

def funcion(ob1, ob2, op1=1, op2=2, *args, **kwargs):
    print("obligatorios:", ob1, ob2)
    print("opcionales: ", op1, op2)
    print("args:", args)
    print("kwargs:", kwargs)
    print()

funcion(10, 20)
funcion(10, 20, op2=200)  # Me salto el op1
funcion(1,2,3,4,5,6,7,8,x=-1, y=-2)

L = [1,2,3,4]
for i in L:
    print(i,end='\t')
