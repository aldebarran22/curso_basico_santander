
from modulos.fecha import Date
from modulos.hora import Time, TimeError
from modulos.fechahora import DateTime, DateTime2

def make_object(clase, *args, **kwargs):
    return clase(*args, **kwargs)


def testFechaHora(clase, *args, **kwargs):
    print("Clase: ", clase.__name__)
    dt = clase(*args, **kwargs)
    print(dt)
    if dt.esBisiesto():
        print("El año es bisiesto")
    else:
        print("No es bisiesto")


def testTimeError():
    try:
        t = Time(12,34,100)
        print(t)
    except Exception as e:
        print(e.__class__.__name__, e)

if __name__ == "__main__":
    testTimeError()
    testFechaHora(DateTime, 24, 4, 2024, 11, 33, 15)
    testFechaHora(DateTime2, 24, 4, 2024, 11, 33, 15)
    
    print("Num instancias: ", Time.getNumInstancias())
    t = Time(2, 4, 34)
    print(t)

    t2 = Time(12, 14, 51)
    print(t2)

    #suma = t + t2  # suma = t.__add__(t2)
    print("Num instancias: ", Time.getNumInstancias())
    #print(suma)

    #del suma  # Fuerza a llamar al destructor: __del__
    print("Num instancias: ", Time.getNumInstancias())

    print(t.__class__)
    print(t.__class__.__name__)

    obj = t.__class__()
    print(obj)

    obj1 = make_object(Time, 12, 34, 8)
    obj2 = make_object(Date, 12, 3, 2024)
    print(obj1)
    print(obj2)
