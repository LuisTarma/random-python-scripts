def find_even_index(arr):
	for i in range(len(arr)):
		t = arr[i]
		arr.pop(i)
		print(arr[:i:], arr[i::])
		if suma(arr[i::]) == suma(arr[:i:]):
			return i
		arr.insert(i, t)
	return -1
def suma(v):
	s = 0
	for i in v:
		s+=i
	return s



a = [1,2,3,4,3,2,1]
print(find_even_index(a))