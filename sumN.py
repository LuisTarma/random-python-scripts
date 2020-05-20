
"""Escribir una funcion recursiva que devuelva la suma de los primeros 
   N enteros
"""

def suma(n):
	if n==0:
		return 0
	s = suma(n-1)
	return (n+s)
	
n = 5
print suma(n)
