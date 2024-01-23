import os


def filtroFicheros(*extensiones, path=None):
    L = os.listdir(path)
    R = []
    for f in L:
        ext = f.partition(".")[-1]
        if ext in extensiones:
            R.append(f)
    return R


if __name__ == "__main__":
    L2 = filtroFicheros("txt", path=r"D:\OneDrive\Escritorio\python_basico_santander\repositorio\codigo_dic_23")
    print(L2)
    L3 = filtroFicheros("py", "txt", "xlsx",path="C:/")
    print(L3)
