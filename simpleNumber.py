
nums = [2,1,2,1,3,2,5,3]
#expected: return 5

def singleNumber(nums):
	for i in range(len(nums)):
		c = nums[i]
		nums[i] = " "
		a = str(nums).find(str(c))
		nums[i] = c
		if a==-1:
			return c		
	return -1

print(singleNumber(nums))
