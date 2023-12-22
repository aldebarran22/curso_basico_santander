import random

for i in range(100):
	numero = random.randint(1,32000)
	nombre = "fich" + str(i) + ".txt"
	f = open(nombre, "w")
	f.write(str(numero))
	f.close
	print(nombre,"grabado ...")
	
	
	
