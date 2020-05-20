
r= [[1,1,2], [1,2,2], [1,4], [3,3,3,4]]
t = 1.3

def ratingThreshold(threshold, ratings):
	c = 0
	s = 0
	l = 0
	f = []
	for i in ratings:
		for j in i:
			s += j
			c += 1
		print(format(s/c, '.2f'), format(threshold, '.2f'))
		if format((s/c), '.2f') == format(threshold, '.2f'):
			l+=1
		s=0
		c=0
	return l
	
print(ratingThreshold(t,r))
