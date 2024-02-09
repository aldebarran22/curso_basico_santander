"""
Prueba del Factorial con Recursividad
"""

def fact(n):
	return 1 if n == 1 else n * fact(n-1)
	
	
	
def test_fact():
	for i in range(2500):
		fact(900)
	

