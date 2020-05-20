l = [5,3,1,3,5]

def isp(l):
	t = []
	#
	if len(l)%2!=0:
		n = len(l)+1
	else:
		n = len(l)-1
	#
	c = (n/2)
	print c
	v = c+1
	i = 0
	while c!=-1: #Agregar la mitad de los elementos a un array diferente
		t.append(l[c])
		c-=1
	while v != n+1:
		print (l[v], " = ", t[i])
		if l[v]!=t[i]:
			print "no es palindromo"
			break
		v+=1
		i+=1
	print t
	
isp(l)
