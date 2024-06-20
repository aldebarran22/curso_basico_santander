AUTHENTICATED = False


def autenticado(f):
    def inner(*args, **kwargs):
        print("Yo autentico")
        if AUTHENTICATED:
            print("Voy a llamar a ", f.__name__)
            f(*args, **kwargs)  # Aqui es donde se ejecuta la funcion abrirPuerta
            print("args", args)
            print("kwargs", kwargs)

        else:
            raise Exception("No tiene permisos de ejecución")

    return inner


def log(f):
    def inner(*args, **kwargs):
        print("en el segundo decorador")
        f(*args, **kwargs)
        print('despues de f en el segundo')

    return inner


@autenticado
def abrir_puerta(a, b, c=0):
    print("en abrir puerta")
    print("a,b,c", a, b, c)


# Programa principal:
try:
    abrir_puerta(1, 2, c=100)

except Exception as e:
    print("Error:", e)
