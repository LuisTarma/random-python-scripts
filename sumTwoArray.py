
def sumOfTwo(a, b, v):
	for i in a:
		for x in b:
			g = i==x
			print(g)
			return g
	return False
    
    
a = [1,2,3]
b = [10, 20, 30, 3]
print(sumOfTwo(a, b, 33))
	
