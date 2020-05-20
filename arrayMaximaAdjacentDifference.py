

def arrayMaximalAdjacentDifference(inputArray):
	a = max(inputArray)
	u = -a
	for i in inputArray:
		print("Elemento: ", i, "Maxima resta: ", u)
		if a-i > u:
			u = a-i
	return u


i = [2, 4,  1, 0]
print(arrayMaximalAdjacentDifference(i))

"""
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3

Given an array of integers, find the maximal absolute difference between any two of its adjacent 
elements.
Input: inputArray: [-1, 4, 10, 3, -2]
Expected Output: 7
"""