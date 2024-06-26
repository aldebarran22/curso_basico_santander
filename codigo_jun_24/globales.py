"""
Variables globales en Python
"""

color = "rojo"

def cambiarColor(nuevoColor):
    global color
    color = nuevoColor

def imprimir():
    print('color: ', color)

if __name__ == "__main__":
    imprimir()
    cambiarColor("verde")
    imprimir()
