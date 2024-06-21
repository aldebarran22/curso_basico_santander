"""
Importar un módulo que no está en la carpeta actual y tampoco
en las carpetas de las librerías de Anaconda / Python
"""

import sys

sys.path.append("C:/temp")

import saludos

saludos.saludar()