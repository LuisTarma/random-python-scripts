
arr = [3,4,1,2,6,5,0,8]
#expected: return 2


def missingNumber(arr):
	ma=arr[0]
	for i in range(1,len(arr)):
		if arr[i]>ma:
			ma=arr[i]
	for i in range(len(arr)):
		a = str(arr).find(str(ma))
		if a==-1:
			return ma
		ma -= 1
	return ma+1

print(missingNumber(arr))
