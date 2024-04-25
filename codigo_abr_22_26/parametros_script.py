"""
Capturar los parámetros de la línea de comandos
y ejecutar una función.
"""

import sys
from funciones_curso import fusion, testFusion

if __name__ == '__main__':
    try:
        if len(sys.argv)==1:
            testFusion()

        elif len(sys.argv)==4:
            fusion(sys.argv[1], sys.argv[2], sys.argv[3])

        else:
            print('Se esperaban 3 parámetros. Sintaxis:')
            print('python parametros_script.py <<path1>> <<path2>> <<pathDestino>>')

    except Exception as e:
        print(e)
