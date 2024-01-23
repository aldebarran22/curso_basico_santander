import os


def filtroFicheros(path, *extensiones):
    L = os.listdir(path)
    R = []
    for f in L:
        ext = f.partition(".")[-1]
        if ext in extensiones:
            R.append(f)
    return R


if __name__ == "__main__":
    L2 = filtroFicheros(".", "py")
    L3 = filtroFicheros(".", "py", "txt", "xlsx")
