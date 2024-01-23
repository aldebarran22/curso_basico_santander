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


def funcion(a, b):
    print("obligatorios: ", a, b)
    print()


def funcion2(a=10, b=20):
    print("opcionales: ", a, b)
    print()


def funcion3(a, b, d, c=0):
    pass


def funcion4(*args):
    print("args: ", args)
    print()


def funcion5(obligatorio, opcional=10, *args, **kwargs):
    print("obligatorio:", obligatorio)
    print("opcional:", opcional)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print()


def plot(**kwargs):
    # Valores por defecto
    d = {"color": "red", "grosor": 1.0}
    d.update(kwargs)
    print("pinta gráfica de color: ", d["color"], "y grosor:", d["grosor"])


if __name__ == "__main__":
    plot(color="green",label="precios")
    exit()
    funcion5(0, 1, 2, 3, 4, 5, x=100, y=200)

    funcion(1, 2)  # forma posicional
    funcion(b=2, a=1)  # forma nominal

    funcion2(b=200)  # forma nominal.
    funcion4(1, 2, 3, 4, 5)  # Se recibe como una tupla
