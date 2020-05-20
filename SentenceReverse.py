
s = "My dog is crazy blue"
#waited crazy is dog my

def reverseSentence(sentence):
	a = (sentence.split(" "))
	i = len(a)-1
	j = ""
	while i!=-1:
		j+=a[i]+" "
		i-=1
	return j
	
print(reverseSentence(s))



