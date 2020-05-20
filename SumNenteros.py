"""Escribir un programa que encuentre la suma de los enteros positivos
   pares desde N hasta 2. Chequear que si N es impar se imprima un 
   mensaje de error.
"""
s=0
def suma(n):
	if n == 2:
		return 0
	if n%2!=0:
		n = n-1
	s = suma(n-1)
	return n+s
	
n = 10
print suma(n)
