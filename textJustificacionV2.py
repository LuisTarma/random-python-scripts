
words = ["This", "is", "an", "example", "of", "text", "justification."]
l = 16
just = []
cont = []

def Just(words, l):
	x = 0
	v = ""
	suma = 0
	for i in words:
		cont.append(len(i))
	for i in range(len(cont)):
		if cont[i] > l:
			continue #Cannot show in display
		if cont[i] <= l:
			suma += cont[i]
			print(suma, cont[i])
			if suma<=l:
				v += words[i]
				just.append(v)
				v = ""
			else:
				suma = 0
				just.append("/n")
				just.append(words[i])
				continue
	return just



print(Just(words, l))
