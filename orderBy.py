#Sort the letters in the string "s" by the order they occur in the string 
# t.
# TODO return string 

s = "caramelo"
t = "bcari"

def sortByString(s, t):
	o = ""
	for i in t:
		for e in s:
			if i==e:
				o += e
	return o

print(sortByString(s,t))
