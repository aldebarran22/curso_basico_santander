"""
Importar un módulo que se encuentra en otra ruta, modificando
sys.path en t.de ejecución
"""

import sys

sys.path.append("C:/temp")

import saludos

saludos.saludar()