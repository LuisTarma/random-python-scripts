
def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
        
    r = potencia(c[:-1])
    #r = [1,2,3]
    a = [s + [c[-1]] for s in r]
    #a = [1]
    n = r + a
    #n = [[] , [1]] 
    #print ("primero: ", n)
    return n
    
def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]
    
c = [1,2,3,4,5]
print combinaciones(c, 3)
