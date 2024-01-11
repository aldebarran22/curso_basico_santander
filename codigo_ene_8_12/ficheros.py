"""
Leer y escribir ficheros CSV con Python
"""
def leerFichero(path):
    """
    Imprimir el contenido en consola
    """
    fich = None
    try:
        # Abrir el fichero en modo lectura
        fich = open(path, "r")
        for linea in fich:
            print(linea)
            
    except Exception as e:
        print(e)
    finally:
        if fich != None: fich.close()

if __name__ == '__main__':
    leerFichero('../ficheros/Pedidos.txt')