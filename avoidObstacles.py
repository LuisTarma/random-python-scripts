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
	l = [x for x in range(max(s)+1)][1::]
	f = []
	c = 0
	a = 0
	while len(s)!=len(l):
		if s[c] == l[a]:
			f.append(0)
			c+=1
		else:
			f.append(a)
		a+=1
	print(l)
	print(f)
	c = 1
	for i in cycle(l):
		mul = i
		for j in range(len(s)):
			print("Salto: ", mul, "Elemento: ", s[j])
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