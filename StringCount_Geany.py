def commonCharacterCount(s1, s2):
    l = []
    s = 0
    a = "a"
    for i in sorted(s1):
        if  i == a:
            a = i
            s += 1
        else:
            s = 0
        l.append(s)
    return l

# print(commonCharacterCount("aabcc", "adcaa"))


def contador(s):
    l = []
    cont = 0
    a = "a"
    for i in sorted(s):
        if a == i:
            cont += 1
            a = i
        else:
            l.append(cont)
            cont = 0
    return l
print(contador("aabbbjjcc"))


#    l = []
#    for i in sorted(s1):
#        for j in sorted(s2):
#            # print("Cadena1: ", i, "Cadena2: ", j, "Cantidad: ", c)
#            if i == j:
#                c += 1
#    return c
