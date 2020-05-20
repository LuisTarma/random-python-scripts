
#1 - Identificar tarjeta
#2 - "Habilitar"
#3 - Comprobacion de contraseña
#4 - Habilitar menu
#5 - Emision de ticket
#6 - Redondeo de billetes Ej: no billetes de 10mil

import os
import getpass

class Cajero:
	def Datos(self, saldo):
		self.saldo = saldo
		#self.can100 = can100
class Usuario:
	def Datos(self, nombre, contrasena, fecha_nac, saldo):
		self.nombre = nombre
		self.contrasena = contrasena
		self.fecha_nac = fecha_nac
		self.saldo = saldo
def Retirar():
	os.system("cls")
	titulo()
	s = Cliente.saldo
	print(" Su saldo disponible es de "+str(s))
	if s<=0:
		print(" No es posible hacer retiros - Saldo insuficiente")
		return
	r = int(input("  Ingresa cantidad a retirar: "))
	if r>s:
		print(" La cantidad sobrepasa el saldo disponible en su cuenta")
		Retirar()
	else:
		Cliente.saldo = s - r
		
		#b = pdf(Detalles_retiro);
		#imprimir(b)
		
		sobra = []
		sobra = CalcularBilletes(r)
		if sobra[0] > 0:
			print(" La cantidad " + str(sobra[0]) + " no puede ser retirada. Se volvera a agregar a su cuenta")
			Cliente.saldo += int(sobra[0])
			print(" Cantidad retirada: "+ str(r-sobra[0]))
			print(" Saldo disponible: "+ str(Cliente.saldo))
def titulo():
	print("----------------------------------------------".center(110, "-"))
	print("----------| CAJERO AUTOMATICO |---------------".center(110, "-"))
	print("----------------------------------------------".center(110, "-"))	
	print(" ")	
def Depositar():
	os.system("cls")
	titulo()
	s = Cliente.saldo
	print(" Su saldo disponible es de "+str(s))
	r = int(input("Ingresa cantidad a depositar: "))
	if r<=0:
		print(" Ingrese una cantidad valida")
		Depositar()
	else:
		Cliente.saldo = s + r
		sobra = []
		sobra = CalcularBilletes(r)
		if sobra[0] > 0:
			print(" La cantidad " + str(sobra[0]) + " no puede ser depositada.")
			Cliente.saldo -= int(sobra[0])
			print(" Cantidad depositada: "+ str(r-sobra[0]))
			print(" Saldo disponible: "+ str(Cliente.saldo))


def CalcularBilletes(monto):
	#x = int(input("Ingresa cantidad: "))
	
	#monto = 520000
	c100 = 0
	c50 = 0
	c20 = 0
	sobra = 0
	while monto>0:
		if monto>=100000:
			c100 += 1
			monto -=100000 # monto = 420000  2) 320000 3) 220000 4) 120000 5) 20000 6)0
		else:
			if monto>=50000:
				c50 += 1
				monto -=50000 # monto = 20000
			else:
				if monto>=20000:
					c20 += 1
					monto -= 20000 # monto = 0
				else:
					sobra = monto
					break
	
	print(" Cantidad de billetes de 100.000 G: "+ str(c100))
	print(" Cantidad de billetes de 50.000 G: "+ str(c50))
	print(" Cantidad de billetes de 20.000 G: "+ str(c20))
	print("Sobra: "+ str(sobra))
	
	
	return [sobra, c100, c50, c20]




def Menu():
	while 1:
		print(" -------------------------------".center(110, " "))
		print(" 1- Retirar Dinero             -".center(110, " "))
		print(" 2- Depositar Dinero           -".center(110, " "))
		print(" 3- Saldo disponible en cuenta -".center(110, " "))
		print(" 4- Cerrar Sesion              -".center(110, " "))
		print(" -------------------------------".center(110, " "))
		op = int(input(" Opcion: ".center(80, " ")))
		if op == 1:
			Retirar()
		elif op == 2:
			Depositar()
		elif op == 3:
			print("Su saldo disponible es: " + str(Cliente.saldo))
			continue
		elif op == 4:
			os.system("cls")
			break
		else:
			print("Ingrese una opcion valida")
def ValidarPin(x):
	pin = getpass.getpass("Ingrese pin: ")
	
	if int(pin) == int(Cliente.contrasena):
		print("Pin correcto")
		Menu()
	else:
		if x>1:
			print("Limite de intentos alcanzado.")
			return 1
		else:
			print("Pin Incorrecto - vuelva a intentarlo")
			x += 1
			ValidarPin(x)

while 1:
	#Datos del cajero
	Caja = Cajero()
	Caja.Datos(4300000)
	titulo()
	print("")
	print(" Ingresa tarjeta de credito".center(110, " "))
	print("")
	s = input("")
	#Datos del cliente prueba
	Cliente = Usuario()
	#Cliente de prueba
	Cliente.Datos("luis", 1234, "02/10/96", 3500000)
	#Comprobacion de pin
	ValidarPin(0)












"""
a = int(input("Numero: "))
c = ""
e = ""
for i in range(a):	
	c += "*"
	if i<a-2:
		e += " "
print(c)
for i in range(a-2):
	print("*"+e+"*") 
print(c)
"""
