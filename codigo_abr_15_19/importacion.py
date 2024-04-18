"""
Modificar la variable path del módulo sys para añadir una nueva ruta 
e importar un módulo que se encuentra en la carpeta D:/temp
"""
import sys

sys.path.append("D:/temp")

import funcion_abc

print(funcion_abc.operar(12,34))