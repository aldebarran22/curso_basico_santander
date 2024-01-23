"""
Importar el módulo funciones_ecuacion y utilizar
la función ecuación.
1) import modulo
2) import modulo as alias
3) from modulo import funcion
"""

"""
# opción 1
import funciones_ecuacion

resul = funciones_ecuacion.ecuacion(1, 5, 4)
print(resul)
"""

"""
# opción 2
import funciones_ecuacion as fe

resul = fe.ecuacion(1, 5, 4)
print(resul)
"""

# opción 3
from funciones_ecuacion import ecuacion

resul = ecuacion(1, 5, 4)
print(resul)
