"""
POO en Python
"""

class Empleado:
    """Implementación de la clase empleado"""

    def __init__(self, id=0, nombre="", cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

def testEmpleado():
    emp = Empleado(12, 'Pedro', 'Ventas')
    print(emp)

if __name__ == "__main__":
    testEmpleado()