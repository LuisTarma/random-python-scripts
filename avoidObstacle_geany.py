"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to 
make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles.
Example
For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
Check out the image below for better understanding:
"""
from itertools import *
def avoidObstacles(inputArray):
	s = sorted(inputArray) # [1, 2, 4, 6, 10]
	l = [x for x in range(max(s)+1)][::]
	print(l)
	for i in s:
		l.pop(i)
		l.insert(i, 0)
	print(l)
	c = 1
	for i in cycle(l):
		mul = i
		for j in range(len(s)):
			#print("Salto: ", mul, "Elemento: ", s[j])
			if mul==s[j]:
				break
			mul += i
		c+=1
		if c==1*max(l):
			break

s = [1, 4, 10, 6, 2] # [1, 2, 4, 6, 10]
print(avoidObstacles(s))
"""
Input: inputArray: [1, 4, 10, 6, 2]
				   [1, 2, 4, 6, 10]
Expected Output: 7
"""
