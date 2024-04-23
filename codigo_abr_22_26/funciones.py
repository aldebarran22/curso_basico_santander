"""
Funciones en python:
Paso de parámetros y tipos de parámetros:
- obligatorios
- opcionales
- tupla
- diccionario

- Tipos anotados
"""


def saludar(nombre):
    """Devuelve un saludo"""
    return "Hola " + nombre.capitalize()


def saludar2(nombre: str) -> str:
    """Devuelve un saludo 2"""
    return "Hola " + nombre.capitalize()


def sumar(a: int = 10, b: str = "") -> str:
    """Multiplica un iterable por un número"""
    return b * a


if __name__ == '__main__':
    print("__name__: ", __name__)
    print(sumar(b="hola"))
    # print(sumar(23, 45))
    # print(sumar("23", "45"))
    print(sumar(3, [45]))
    print()
