import math
def is_square(n): 
    a = math.sqrt(n)
    print(a**2, int(a)**2)
    if a**2==int(a)**2:
    	return True
    return False







print(is_square(26))
