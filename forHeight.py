

def sortByHeight(a):
    pos, sor, nuv = [], [], []
    for i in range(len(a)):
        if a[i] == -1:
            pos.append(i)
        else:
            sor.append(a[i])
    sor = sorted(sor)
    pos.append(0)
    s, v = 0, 0
    try:
        for i in range(len(a)):
            if i == pos[v]:
                nuv.append(-1)
                v += 1
            else:
                nuv.append(sor[s])
                s += 1
        return nuv
    except:
        return sor

a = [4, 2, 9, 11, 2, 16]
print(sortByHeight(a))