
s = [1,1,2]
#expected: return false (Nothing can be removed for leave a Increasing Sequence)

def almostIncreasingSequence(sequence):
	i = 0
	while i!=len(sequence):
		a = sequence[i]
		sequence.pop(i)
		v = 1
		f = 0
		while v!=len(sequence):
			if sequence[v]<=sequence[f]:
				return False
			v +=1
			f +=1
		sequence.insert(i, a)
		i+=1
	return True

print(almostIncreasingSequence(s))


#sorted(iterable, cmp=None, key=None, reverse=False)
"""
	c = 0
	for i in range(len(sequence)):
		v = sequence.count(sequence[i])
		if v>=3:
			return False
	for i in range(len(sequence)):
		a = sequence[i]
		sequence.pop(i)
		order = sorted(sequence)
		print(sequence, order)
		if sequence == order:
			return True
		sequence.insert(i, a)
	return False
"""
