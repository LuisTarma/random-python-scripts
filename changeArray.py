
def arrayChange(inputArray):
	c = 0
	while True:
		i=0
		for i in range(len(inputArray)):
			try:
				print(inputArray[i], inputArray[i+1])
				if inputArray[i] >= inputArray[i+1]:
					inputArray[i+1] += 1
					c+=1
					i+=1
			except:
				return c
		if i==0:
			break
	return c

a = [2, 1, 10, 1]
print(arrayChange(a))
#return 12
