# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
l=[1,2,3,4,3,2,1]

def isp(l):
	n = len(l)-1
	for i in xrange(n):
		print (l[i], " = ", l[n-i])
		if l[i] != l[n-i]:
			print "No es palindromo"
			break
isp(l)
