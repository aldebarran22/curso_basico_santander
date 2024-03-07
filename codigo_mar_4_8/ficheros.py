def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for line in fich:
            print(line)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    leerFichero("../ficheros_curso/Pedidos.csv")
