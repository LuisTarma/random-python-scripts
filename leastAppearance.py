def leastAppearance(choices):
	l = []
	m = []
	for i in choices:
		m.append(list(set(i)))

	for i in m:
		if min(i) not in l:
			l.append(min(i))
		else:
			i.pop(i.index(min(i)))
			l.append(min(i))
	c = 0
	for i in choices:
		if min(i) != l[c]:
			l[c] = min(i)
		c+=1
	return l


a =  [[1,2], [3,4], [1,2]]
print(leastAppearance(a))