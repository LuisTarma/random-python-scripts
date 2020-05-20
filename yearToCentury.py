
y = 201
#expected: return 20

def centuryFromYear(year):
	a = year/100
	if a>int(a):
		return int(a)+1
	return int(a)
	
print(centuryFromYear(y))

c = input(" ")
