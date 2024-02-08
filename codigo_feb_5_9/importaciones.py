"""
Importar un módulo de Python que no está en la 
carpeta actual y tampoco en las lib de python
"""
import sys

sys.path.append('D:/temp')
import funcion_abc
print(funcion_abc.operar(12,34))



