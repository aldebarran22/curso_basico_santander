"""
Importar un módulo que está fuera de la carpeta
de code y tampoco está en las librería de Python
"""
import sys

sys.path.append(r"D:\temp")
from funcion_abc import operar

print(operar(1, 4))
