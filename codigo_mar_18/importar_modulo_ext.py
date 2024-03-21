"""
Modificar la variable PYTHONPATH para añadir una nueva ruta de búsqueda
y poder importar un módulo que se encuentra en otra carpeta.
"""

import sys

sys.path.append("D:/temp")

import funcion_abc

print("operar: ", funcion_abc.operar(12, 34))
