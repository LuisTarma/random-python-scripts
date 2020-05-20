# Coincidencias en s del string x

s = "Mydogiscrazy"
x = "dog"

def strstr(s, x):
	e = 0
	for i in s:
		#print(i)
		for j in x:
			print(j)
			#if i!=j:
				#print(i)
				#break
			#else:
			#	e+=1
				#print(i)
	return e
	
print(strstr(s, x))
#Use .find(x)
		
