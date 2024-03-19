"""
Importar el módulo de funciones y ejecutar 
una función.
"""


import funciones
print(funciones.filtroFicheros('txt'))


import funciones as f
print(f.filtroFicheros('txt'))


# from modulo import funcion
from funciones import filtroFicheros
print(filtroFicheros('txt'))