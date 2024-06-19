"""
Paso de parámetros a las funciones:
- por copia: los inmutables: int, float, complex, bool, str, tuple
- por ref: los mutables: list, set, dict
"""

def porCopia(numero, tupla, cadena):
    numero += 10
    tupla += (10,100,1000)
    cadena += "1000"

if __name__ == '__main__':
    num = 100
    tupla = 1,2,3
    cad = "hola"

    print(num, tupla, cad)
    porCopia(num, tupla, cad)
    print(num, tupla, cad)

