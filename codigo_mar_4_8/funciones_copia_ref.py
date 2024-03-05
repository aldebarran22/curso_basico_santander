"""
Parámetros por copia/valor y referencia
"""

def porCopia(cadena, numero, tupla):
    cadena += "mas texto"
    numero *= 2
    tupla += (9,9,9)

if __name__ == "__main__":
    num = 10
    cad = "hola"
    t = 1,2,3

    porCopia(cad, num, t)
    print(cad, num, t)
