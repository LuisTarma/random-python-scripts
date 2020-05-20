

"""
def alternatingSums(a):
	s1 = 0
	s2 = 0
	for i in range(len(a)):
		if i%2==0 :
			s1 += a[i]
		else:
			s2 += a[i]
	s = []
	s.append(s1)
	s.append(s2)
	return s
"""
def alternatingSums(a):
	return a[1::2]

a = [50, 60, 60, 45, 70]
print(alternatingSums(a))

# return [180, 105]
