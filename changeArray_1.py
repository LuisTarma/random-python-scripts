
from itertools import *
def arrayChange(inputArray):
    i = 1
    suma = 0
    while i < len(inputArray):
        if inputArray[i] <= inputArray[i-1]:
            suma += (inputArray[i-1] - inputArray[i]) + 1
            inputArray[i] += (inputArray[i-1] - inputArray[i]) + 1 
        i += 1
    return suma

a = [2, 1, 10, 1]
print(arrayChange(a))
#return 12
"""
def arrayChange(inputArray):
	c = 1
	x = 0
	o = 0
	for i in cycle(inputArray):
		print("Array1=", i, "Array2=", inputArray[c])
		if i >= inputArray[c]:
			inputArray[c] += 1
			x += 1
		c += 1
		o += 1
		if c==len(inputArray):
			c=1
			print(" ")
		if o==80:
			break
	return x
"""
