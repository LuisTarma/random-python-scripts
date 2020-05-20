
a = 20000
b = 50000
c = 100000

x = int(input("Cantidad: "))
while 1:
	p = 0
	if x%a==0:
		p += a
		print("puede: "+str(p))
	if x%b==0:
		p += b
	if x%c==0:
		p += p
	else:
		print("No puede depositar: "+ str(x) +" pero puede depositar: " + str(p))
		
