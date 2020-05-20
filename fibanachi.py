
s = "luis"
def fibo(n):
	s = s + ""
	if n==0:
		return 0
	if n==1:
		return 1
	return fibo(n-1)+ fibo(n-2)

x = 10

for i in range(10):
	print(fibo(i))
