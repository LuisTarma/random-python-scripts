
def operar(numero1, numero2):
	if(numero2 == 0):
		return numero1
	elif(numero2 < 0):
		return operar(numero1-1, numero2+1)
	else:
		return operar(numero1+1, numero2-1)
     
     
if __name__ == "__main__":
	print("Sumando 10 y 3:", operar(10, 3))
	print("Sumando 5 y -2:", operar(5, -2))
