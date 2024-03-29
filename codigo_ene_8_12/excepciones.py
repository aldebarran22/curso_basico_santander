"""
Capturar y lanzar excepciones en Python
"""
import os


def prueba1():
    # Capturar un única excepción y tratarla
    try:
        L = [1, 2, 3, 4, 5]
        print("Pos 100:", L[100])
        print("Longitud de L:", len(L))
    except IndexError as e:
        print(e)


def prueba2():
    # Capturar dos excepciones distintas
    try:
        L = [1, 2, 3, 4, 5]
        d = {"a": 1, "b": 2}
        print(d["x"])  # KeyError
        print("Pos 100:", L[100])  # IndexError
        print("Longitud de L:", len(L))
    except IndexError as e:
        print(e)
    except KeyError as e:
        print("No existe la clave del dict: ", e)


def prueba3():
    # Capturar dos excepciones distintas y otras posibles excepciones
    try:
        L = [1, 2, 3, 4, 5]
        d = {"a": 1, "b": 2}
        print(L[2] / 0)
        print(d["x"])  # KeyError
        print("Pos 100:", L[100])  # IndexError
        print("Longitud de L:", len(L))
    # except (IndexError, KeyError) as e:
    except IndexError as e:
        print(e)
    except KeyError as e:
        print("No existe la clave del dict: ", e)
    except Exception as e:
        print(e.__class__.__name__, e)


def procesarFichero(f):
    # Extraer la extensión del fichero y
    # si no es python lanzar excepción
    t = f.partition(".")
    if t[2] != "py" and t[2] != "":
        raise Exception(f"Error al procesar el fichero: {f}")
    else:
        print(f"procesando el fichero {f}")


def prueba4():
    # Procesar los ficheros de una carpeta y
    # generar un error al azar en uno de los
    # ficheros.
    errores = 0
    ficheros = os.listdir()
    for f in ficheros:
        try:
            procesarFichero(f)
        except Exception as e:
            print(e)
            errores += 1
    print(f"Total ficheros {len(ficheros)} y errores: {errores}")


def prueba5():
    # Comprobar como se ejecuta finally antes de hacer el return
    try:
        print("todo bien")
        raise Exception("fallo")
        return True

    except Exception as e:
        print(e)

    finally:
        print("finally")


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    # prueba4()
    prueba5()
