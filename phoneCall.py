

def phoneCall(min1, min2_10, min11, s):
	t = 0
	if min1<=s:
		t+=1
		s-=min1
	while s>0:
		if t<=10:
			t+=1
			s-=min2_10
		if t>10:
			t+=1
			s-=min11
		print("Minuto: ", t, "Resta: ", s)
	return t

print(phoneCall(1,2,1,6))

"""

"""


