"""
Función format y fstring
Rellenos en fechas y horas:
2:6:23 -> 02:06:23
1/1/2024 -> 01/01/2024
"""


def fechaHora(d=1, m=1, y=1970, H=0, M=0, S=0):
    resul = "%02d/%02d/%04d %02d:%02d:%02d" % (d, m, y, H, M, S)
    return resul

# Generar rutas de nombres de ficheros:
# c:/paises/suiza.csv, c:/paises/finlandia.csv,
def generarPath(pais):
    path = "c:/paises/{}.csv".format(pais.lower())
    # otra forma: con fstring
    path = f"c:/paises/{pais.lower()}.csv"
    return path

if __name__ == "__main__":
    print(fechaHora(m=10, M=45))
    L = ["Suiza", "Alemania", "Francia", "España"]
    for p in L:
        print(generarPath(p))
