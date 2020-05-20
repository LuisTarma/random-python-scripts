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
