"""Programe un metodo recursivo que calcule la suma de un arreglo de
   numeros enteros.
"""

def suma(l):
	if len(l) == 0:
		return 0
	s = suma(l[:-1])
	return l[len(l[:-1])]+s
	
l=[1,2,3,4,5]
print suma(l)
