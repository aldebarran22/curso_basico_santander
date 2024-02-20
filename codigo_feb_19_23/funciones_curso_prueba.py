"""
Importar funciones del módulo: funciones_curso.py
"""

"""
# opción 1
import funciones_curso

print(funciones_curso.sumaResta(1,2))
"""

"""
# opción 2: importar con un alias
import funciones_curso as f

print(f.sumaResta(1, 2))
"""

# opción 3: importar directamente la función
# from modulo import función
#from funciones_curso import sumaResta, ecuacion, filtroFicheros
#print(sumaResta(1,2))

import funciones_curso as f
import funciones_curso2 as f2
print(f.sumaResta(1, 2))
print(f2.sumaResta(1, 2))