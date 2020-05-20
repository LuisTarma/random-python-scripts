"""
Two arrays are called similar if one can be obtained from another by swapping at
most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.

Example:
For a = [1, 2, 3] and b = [1, 2, 3], the output should be areSimilar(a, b) = true.
The arrays are equal, no need to swap any elements.
	For a = [1, 2, 3] and b = [2, 1, 3], the output should be areSimilar(a, b) = true.
We can obtain b from a by swapping 2 and 1 in b.
	For a = [1, 2, 2] and b = [2, 1, 1], the output should be areSimilar(a, b) = false.
Any swap of any two elements either in a or in b won't make a and b equal.

"""
import os
def areSimilar(a, b):
	l = [] #Indices de desiguales
	for i in range(len(a)):
		if a[i]!=b[i]:
			l.append(i)
	if len(l)>2:
		return False
	elif len(l)==0:
		return True
	else: #Quiere decir que hay dos iguales
		#print(l)
		temp = a[l[0]]
		a[l[0]] = a[l[1]]
		a[l[1]] = temp
		if a==b:
			return True
		else:
			return False
a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
print(areSimilar(a, b))
#return false
os.system("pause")
"""
a: [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b: [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

return true
"""
