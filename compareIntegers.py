"""
def compare(a, b):
	a,b = map(int,eval(dir()[0]))
	return ("elqeusasl"[a < b::2],"greater")[a > b]
"""
def compare(a, b):
	a,b = map(int,eval(dir()[0]))
	return a>b and 'greater' or 'elqeusasl'[a<b::2]


print(compare(1, 6))
