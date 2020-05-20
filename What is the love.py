
l = ["What", "is", "love?", "Baby", "don't", "hurt", "me", "Don't", "hurt", "me", "no", "more"]


#whatIsLove = (9**5*" what   baby don't hurt me don't   no ").split(" ").pop

whatIsLove = lambda n : "  what      baby    hurt  me        no".split('  ')[n%12] or "don't"
print(whatIsLove(23))

def whatIsLove(n):
    song = "What is love? Baby don't hurt me Don't hurt me No more"
    song = song.lower().replace('\n','')
    haddaway = song.split(' ')
    return haddaway[(n-1)%len(haddaway)]
    
def whatIsLove(n):
    lyrics = "what is love baby don't hurt me don't hurt me no more"
    lyric_list = lyrics.split()
    size = len(lyric_list)
    lyric = lyric_list[(n%size)-1] 	
    print(lyric)
    return lyric
def whatIsLove(n):
    """Return lyrics of What is Love."""
    haddaway = """
What is love?
Baby don't hurt me
Don't hurt, me no more"""
    h_list = haddaway.split()
    h_list *= 50000
    return h_list[n-1].lower()
"""
def whatIsLove(n):
	c=1
	a=n
	while a!=0:
		for i in l:
			print(n, c)
			if n==c:
				return i
			c+=1
		a-=1


print(whatIsLove(1237))
"""


"""
What is love?

Yeah, yeah

(Ooh, ooh)

I don't know why you're not there
I give you my love, but you don't care
So what is right?
And what is wrong?
Gimme a sign

What is love?
Baby, don't hurt me
Don't hurt me no more
"""
