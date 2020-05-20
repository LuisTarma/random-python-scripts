
s = [2,4,5,6,8,10,11]
#expected: return 2 (3,7)

def makeArrayConsecutive2(statues):
	#No mames men
	v = sorted(statues)
	i = v[0]
	a = max(statues)
	c = 0
	while i != a: 
		r = i+1
		print(r,i,c)
		if not r in v:
			c +=1
		i += 1
	return c

print(makeArrayConsecutive2(s))


"""
	m = statues[0]
	a = 0
	if len(statues)==1:
		return 0
	for i in range(len(statues)):
		if statues[i]>m:
			m = statues[i]
	mi = m
	for i in range(len(statues)):
		if mi>statues[i]:
			mi = statues[i]
	for i in range(m):
		m -= 1
		if m == mi:
			break
		if str(statues).find(str(m))==-1:
			a += 1
		print(m, str(statues).find(str(m)), i, mi)
	return a
"""
