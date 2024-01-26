import sys

def imprimir():
	print('Estoy en el paquete prueba.pruebas')
	sys.path.append('../..')
	from  excepciones.CajeroException import CajeroException
	
	raise CajeroException('dentro de pruebas.prueba')


try:
	imprimir()
except Exception as e:
	print("ERROR: " + str(e))
