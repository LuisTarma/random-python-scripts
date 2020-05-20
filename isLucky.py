
# 1230 true
# 1424 false

def isLucky(n):
    l = [int(c) for c in str(n)]
    tam = int(len(l)/2)
    suma1 = 0
    for i in range(tam):
        suma1 += int(l[i])
    a = tam
    suma2 = 0
    while a != len(l):
        suma2 += int(l[a])
        a+=1
    if suma1 != suma2:
        return False
    else:
        return True

print(isLucky(1231))