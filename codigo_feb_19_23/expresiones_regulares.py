"""
Expresiones regulares en Python
"""
import re

def validar(patron, L):
    print('Patrón: ', patron)
    for cad in L:
        resul = True if re.match(patron, cad) != None else False
        print(cad,' -> ', resul)
    print("-"*20)

if __name__ == '__main__':
    patron=""
    L = [""]
    validar(patron, L)