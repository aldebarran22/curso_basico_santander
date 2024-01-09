"""
Definición de parámetros dentro de una función
"""
def funcion(ob1, ob2, op1=1, op2=2):
    print('obligatorios: ', ob1, ob2)
    print('opcionales:', op1, op2)
    print()

if __name__ == '__main__':
    funcion(10,20)
    funcion(10,20,30,40)

