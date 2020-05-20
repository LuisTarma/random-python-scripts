n = raw_input("Ingresa texto :v ")
pal = "";
cont=0
v = []
for i in xrange(len(n)):
	v.append(n[i])
	if v[i]=="v":
		cont+=1
		v[i]="*"
	pal+= v[i]
print "Veces encontrado:v ",cont
print pal
	
