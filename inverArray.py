"""
	Programe un metodo recursivo que invierta los numeros de un arreglo
	de enteros.
"""

def inv(l):
	if len(l)==0:
		return 0
	i = inv(l[:-1])
	return [s for s in i]
	
	
l = [1,2,3,4,5]
print inv(l)
