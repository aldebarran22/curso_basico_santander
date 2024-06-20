"""
Listar el contenido de un fichero que nos envían como
parámetro
"""
import sys

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r", encoding="cp1252")
        txt = fich.read()
        print(txt)

    except Exception as e:
        raise e

    finally:
        if fich: fich.close()

if __name__=='__main__':
    if len(sys.argv) == 2:
        leerFichero(sys.argv[1])
    else:
        print('Falta un parámetro: ')
        print('python listar.py path_fichero')