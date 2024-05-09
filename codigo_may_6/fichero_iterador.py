# Leer un fichero con un iterador:

print("Imprimir el contenido de un archivo")
with open("fusion_ficheros.py") as fp:
	for linea in iter(fp.readline,''):
		print(linea)


