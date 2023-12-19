"""
Función format y fstring
"""

# Generar rutas de nombres de ficheros:
# c:/paises/suiza.csv, c:/paises/finlandia.csv, 
def generarPath(pais):
    path = "c:/paises/{}.csv".format(pais.lower())
    # otra forma: con fstring
    path = f"c:/paises/{pais.lower()}.csv"
    return path

if __name__ == '__main__':
    L = ['Suiza','Alemania','Francia', 'España']
    for p in L:
        print(generarPath(p))