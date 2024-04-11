"""
Importar un módulo que está fuera de pythonpath
"""
import sys

sys.path.append("C:/temp")

import saludos
saludos.saludar()
