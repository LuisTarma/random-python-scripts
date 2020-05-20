
s = "bcabbacb"
#expected: return true

def checkPalindrome(inputString):
	m = len(s)-1
	for i in range(int(len(s)/2)):
		if inputString[i]!=inputString[m]:
			return False
		m-=1
	return True

print(checkPalindrome(s))
