"""
Modificar la variable PYTHONPATH añadiendo
una ruta de otra carpeta en t.de ejecución
"""

import sys

# Añadir la carpeta donde está el módulo al path
# de Python
sys.path.append("D:/temp")

import funcion_abc
print("operar: ", funcion_abc.operar(100,300))
