"""
Funciones en Python:
Llamar a una función:
- 1) Forma posicional
- 2) Forma nominal
- 3) A partir de una tupla / lista
- 4) A partir de un diccionario

Tipos anotados.
"""

def segundos(h=0, m=0, s=0):
    return h*3600 + m*60 + s

def sumar(a,b):
    return a+b

def ejemplo():
    """Documentación de la función ejemplo"""
    pass

ejemplo()

# 1) posicional
print(sumar(1,2))
# 2) nominal
print(sumar(b=2, a=1))
print(segundos(m=40))