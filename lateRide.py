def lateRide(n):
    h, m = 0, 0
    while n >= 0:
        if n>=60:
            h +=1
        else:
            m = n
        n-=60
    return sum([int(i) for i in str(h)])+sum([int(i) for i in str(m)])
    
    
print(lateRide(240))
