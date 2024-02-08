"""
Tratamiento de ficheros en Python
Leer / escribir en fichero y redirigir la salida
estandar a un fichero
"""
def printFile():
    f = open("exportaciones/prueba.txt","w")
    print("mensaje de prueba",file=f)
    f.close()


if __name__ == '__main__':
    printFile()