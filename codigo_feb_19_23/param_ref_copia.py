"""
Parámetros por referencia (los mutables)
P. por copia (los inmutables)
"""

def funcion(numero, lista):
    numero += 100
    lista.append(100)

if __name__ == '__main__':
    numero = 1
    L = [1,2,3]
    print(f'numero: {numero}, lista: {L}')
    funcion(numero, L)
    print(f'numero: {numero}, lista: {L}')
