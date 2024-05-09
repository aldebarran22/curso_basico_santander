"""
Importar un módulo que no está en las rutas habituales de búsqueda
"""

import sys

sys.path.append("D:/temp")

import funcion_abc

print(funcion_abc.operar(12, 34))
