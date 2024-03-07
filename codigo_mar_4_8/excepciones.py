"""
Captura de errores.
try, except, finally, raise
"""

def prueba1():
    # Capturar una excepción concreta
    try:
        L = [1,2,3,4]
        print(L[20])
        print('mas codigo')
    except IndexError as e:
        print(e)   

if __name__ == '__main__':
    prueba1()