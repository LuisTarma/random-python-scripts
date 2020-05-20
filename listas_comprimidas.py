#a = [a for a in range(10) if a%2==0]


l = [1,2,3,4]

def potencia(l):
	r = potencia(l[:-1])
	return [r + [s+[c[:-1]] for s in r]


print potencia(l)


