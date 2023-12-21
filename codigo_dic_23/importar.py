"""
Modificar en tiempo de ejecución la propiedad
path del módulo sys para importar un módulo
que se encuentra en otra carpeta.
"""
import sys

sys.path.append('D:/temp')

import funcion_abc

print(funcion_abc.operar(1,2))