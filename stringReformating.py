
s = "1234567"
k = 4

def stringReformatting(s, k):
	a = s.replace("-", "")
	c = ""
	x = 0
	v = k
	if len(s)%2!=0:
		k = v - (len(s)//k-1)
	for i in a:
		c += i 
		if x==(k-1):
			c+= "-"
			x = 0
			k=v
			continue
		x+=1
	return c
	
	
print(stringReformatting(s,k))
