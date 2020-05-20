
words = ["This", "is", "an", "example", "of", "text", "justification."]
l = 16
temp = []

def cont(words, l):
	d = l
	j = 0
	m = 0
	x = ""
	a = []
	for i in words:
		for x in i:
			temp.append(x)
		temp.append(" ")
	while j <= len(temp): #42
		while l!=0:       #16
			#print temp[m], m
			try:
				x += temp[m]
			except:
				break
			l -= 1
			m += 1
		a.append(x)
		x = ""
		l = d
		j += m
		if j>len(temp):
			j-=l
		#print j
	return a

def Justificacion(words, l):
	x=l
	for i in range(len(words)):
		while l != 0:
			justificado.append(words[i])
			l -= 1
	l=x
	return justificado
	
#print Justificacion(words, l)
print cont(words, l)

#v = "luis"
#print v.zfill(10)
