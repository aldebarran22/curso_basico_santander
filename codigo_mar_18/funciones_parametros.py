"""
Tipos de parámetros en las funciones de python:
- obligatorios
- opcionales
- número indeterminado (tupla)
- número indeterminado con claves (diccionario)
Tipos anotados
"""


# Uno obligatorio y otro opcional:
def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)


# Tipos anotados:
def sumar(a: str, b: str) -> str:
    """Concatena o suma los dos parámetros"""
    return a + b


# Tipos de parámetros en la función:
def funcion(ob1, ob2, op1=10, op2=20, *args, **kwargs):
    print("obligatorios: ", ob1, ob2)
    print("opcionales: ", op1, op2)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print()


print(calcularIVA(100))
print(calcularIVA(100, 4))
print(sumar("hola", "adios"))
print(sumar(12, 34))

###
funcion(1,2)
funcion(1,2,3,4,5,6)
funcion(1,2,3,4,5,6,x=10, y=20)