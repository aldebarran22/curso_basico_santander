"""
Importar funciones de otros módulos y probarlas
"""

"""
import funciones_curso
# modulo.funcion
print(funciones_curso.ecuacion(1,5,4))
"""

"""
# Con un alias en el módulo:
import funciones_curso as fc
# alias.funcion
print(fc.ecuacion(1,5,4))
"""

# from modulo import funcion
from funciones_curso import ecuacion

print(ecuacion(1, 5, 4))
