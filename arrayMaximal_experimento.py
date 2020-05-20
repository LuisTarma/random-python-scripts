import random as r

def arrayMaximalAdjacentDifference1(inputArray):
	if len(inputArray)<=2:
		return 0
	a = maximo(inputArray)
	b = maximo(inputArray[::-1])
	if a>b:
		return a
	return b
def maximo(inputArray):
	a = inputArray[0]
	u = -(max(inputArray))
	for i in inputArray[1::]:
		if abs(a-i) > u:
			u = abs(a-i)
		a = i
	return u

def arrayMaximalAdjacentDifference(inputArray):

	max = 0
	long = len(inputArray)
	for i in range(1,long-1):
		if abs( inputArray[i] - inputArray[i-1] ) > max:
			max = abs( inputArray[i] - inputArray[i-1] )
		if abs( inputArray[i] - inputArray[i+1] ) > max:
			max = abs( inputArray[i] - inputArray[i+1] )
	return max

l = []
while True:
	for i in range(6):
		l.append(r.randrange(-10, 10))
	print(l)

	a = arrayMaximalAdjacentDifference(l)
	b = arrayMaximalAdjacentDifference1(l)
	#print(a)
	#print(b)
	if a!=b:
		print("SIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
		break
"""
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3

Given an array of integers, find the maximal absolute difference between any two of its adjacent 
elements.
Input: inputArray: [-1, 4, 10, 3, -2]
Expected Output: 7
"""
