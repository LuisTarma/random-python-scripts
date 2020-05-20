"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""

def palindromeRearranging(inputString): # "abbcabb"
	a = contador(inputString)
	ips = 0
	for k, v in a.items():
		if v%2 != 0:
			ips += 1
	if ips > 1:
		return False
	return True

def contador(s):
    l = sorted([i for i in s])
    m = [] #lista sin repeticion
    m = [a for a in l if m.count(a)==0]
    diccio = dict.fromkeys(m)
    for s in m:
        diccio[s] = l.count(s)
    return diccio

inputString = "abbccddabbaee"
print(palindromeRearranging(inputString))

"""
"abbcabb"
true
""" 