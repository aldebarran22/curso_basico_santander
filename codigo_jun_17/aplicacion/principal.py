
from modulos.producto import Producto
from modulos.productoCRUD import ProductoCRUD

if __name__=="__main__":
    try:
        bd = ProductoCRUD("../../empresa3.db")
        prod = bd.read(1)
        print(prod)

        prod.precio = 2.5
        prod.existencias = 50
        if bd.update(prod):
            print('Registro actualizado')
        else:
            print('No se ha podido actualizar')

        L = bd.select("Bebidas")
        print(len(L), "productos")
        print(L[:3])

        if bd.delete(88):
            print('producto borrado')
        else:
            print('no se ha podido eliminar')

        """
        nuevo = Producto(0, "ColaCola3", 1, 1.8, 230)
        if bd.create(nuevo):
            print('Registro creado: ', nuevo.id)
        else:
            print('no se ha creado')
        """

    except Exception as e:
        print(e.__class__.__name__, e)