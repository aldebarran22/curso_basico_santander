"""
Listar el contenido de un fichero que nos envían como
parámetro
"""
import sys

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        print(txt)

    except Exception as e:
        raise e

    finally:
        if fich: fich.close()

if __name__=='__main__':
    print(sys.argv)