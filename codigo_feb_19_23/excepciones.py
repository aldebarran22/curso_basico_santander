"""
Captura de excepciones en Python
try except finally
raise
"""
from os import listdir

def prueba1():
    try:
        b = 10
        L = [1,2,3,4]
        print(L[1])
        print(L[0] / b)
    except Exception as e:
        print(e.__class__.__name__, e)

def procesarFich(path):
    ext = path.partition('.')[2]
    if ext == 'ipynb':
        raise ValueError(f'Error al procesar el fichero: {path}')
    else:
        print(f'Se ha procesado el fichero: {path}')

def prueba2():
    try:
        for f in listdir():
            procesarFich(f)
    except Exception as e:
        print(e.__class__.__name__, e)



if __name__ == "__main__":
    #prueba1()
    prueba2()