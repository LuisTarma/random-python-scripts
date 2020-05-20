def contador(s):
    l = sorted([i for i in s])
    m = [] # lista sin repeticion # Usar como secuencia para el diccionario
    z = [] # lista de cantidad
    for a in l:
        if m.count(a) == 0:
            m.append(a)
    diccio = dict.fromkeys(m)
    for s in m:
        diccio[s] = l.count(s)
        z.append(l.count(s))
    return diccio

def commonCharacterCount(s1, s2):
    a = contador(s1)
    b = contador(s2)
    cont = 0
    for (k1, v1) in a.items():
        for (k2, v2) in b.items():
            if k1 == k2:
                if v1<=v2:
                    cont+=v1
                else:
                    cont+=1
                print(k1,v1,k2,v2)
    return cont


print(commonCharacterCount("zzzzzaa", "zzzzzzzzzaa"))

# print(contador("aaabbddccc"))






#    l = []
#    for i in sorted(s1):
#        for j in sorted(s2):
#            # print("Cadena1: ", i, "Cadena2: ", j, "Cantidad: ", c)
#            if i == j:
#                c += 1
#    return c
