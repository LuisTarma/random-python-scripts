

def addBorder(picture):
	t = len(picture[0])+2
	l = []
	s = ""
	while len(s)!=t:
		s+="*"
	for i in picture:
		y = str(i[::-1]) + "*"
		l.append(str(y[::-1])+"*")
	a = l[::-1]
	a.append(s)
	b = a[::-1]
	b.append(s)
	return b

picture = ["abc",
           "ded",
           "asd"]
print(addBorder(picture))

"""
addBorder(picture) = ["*****",
					  "*abc*",
					  "*ded*",
					  "*****"]
"""
