# http://es.stackoverflow.com/q/23328/127
import cProfile, pstats, io
     
def ne(x):
	if x != 'val':
		pass
     
def en(x):
	if not x == 'val':
		pass
     
def ee(x):
	if x == 'val':
		pass
	else:
		pass

x = 'valor diferente'
pr = cProfile.Profile()
pr.enable()
for i in range(500000):
	ne(x)
	en(x)
	ee(x)

pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
