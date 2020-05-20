def CalcularBilletes(monto):
	#monto = int(input("Ingresa cantidad: "))

	c100 = 0
	c50 = 0
	c20 = 0
	sobra = 0
	
	#while monto>0:
	
	for i in range(monto):
		
		if monto>=100000:
			c100 += 1
			monto -=100000
		else:
			if monto>=50000:
				c50 += 1
				monto -=50000
			else:
				if monto>=20000:
					c20 += 1
					monto -= 20000
				else:
					sobra = monto
					break
	
	print(" Cantidad de billetes de 100.000 G: "+ str(c100))
	print(" Cantidad de billetes de 50.000 G: "+ str(c50))
	print(" Cantidad de billetes de 20.000 G: "+ str(c20))
	print("Sobra: "+ str(sobra))

CalcularBilletes(470000)
