AUTHENTICATED = True


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



@autenticado
def abrir_puerta(a, b):
    print("en abrir puerta")
    print("a,b", a, b)
   

# Programa principal:
try:
    abrir_puerta(1, 2)

except Exception as e:
    print("Error:", e)
