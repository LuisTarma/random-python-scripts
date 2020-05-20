
n = [1,1,1,2]
#expected: return 20

def adjacentElementsProduct(inputArray):
	m = inputArray[0] * inputArray[1]
	i = 1
	while i!=len(n):
		try:
			if inputArray[i]*inputArray[i+1]>m:
				m = inputArray[i]*inputArray[i+1]
		except:
			pass
		i+=1
	return m

print(adjacentElementsProduct(n))
