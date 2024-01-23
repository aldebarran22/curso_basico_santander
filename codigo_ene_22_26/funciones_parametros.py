"""
Tipos de parámetros en una función.
- Obligatorios
- Opcionales: Se inicializan en la cab. de la función
- Número indeterminado de params: tupla *args
- Número indeterminado de params con clave: dict **kwargs

Tipos de llamada  a una función(con respecto a los parámetros):
- Posicional
- Nominal: con los nombres de los parámetros
"""

def funcion(a,b):
    print('obligatorios: ',a,b)
    print()

def funcion2(a=10, b=20):
    print('opcionales: ',a,b)
    print()

if __name__ == '__main__':
    funcion(1,2)        # forma posicional
    funcion(b=2, a=1)   # forma nominal

    funcion2(b=200)

