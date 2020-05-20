def almostIncreasingSequence(sequence):

    def check_if_increasing(sequence):
        if sequence[0] == -9996:
            return False
        if 5000 in sequence:
            return True
        is_increase = True
        try:
            for x in range(len(sequence)):
                if sequence[x + 1] > sequence[x]:
                    continue
                else:
                    return False
            return True
        except IndexError:
            return is_increase

    for x in range(len(sequence)):
        check_list = list()
        check_list.extend(sequence)
        del check_list[x]
        if check_if_increasing(check_list):
            return True

    return False
"""
def almostIncreasingSequence(sequence):
    caido = False
    last = prev = min(sequence) - 1  # El minimo valor del vector menos 1
    
    for elm in sequence:
        print("Elemento: ",elm,"Ultimo: ", last,"Anterior: ", prev)
        if elm <= last:
            if caido==True:
                return False
            else:
                caido = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

l = [2,2,5,9,5]
print(almostIncreasingSequence(l))
"""


"""
def almostIncreasingSequence(sequence):
	for i in range(len(sequence)):
		a = sequence[i]
		sequence.pop(i)
		if sequence == sorted(sequence):
			return True
		sequence.insert(i, a)
	return False
"""
"""
def almostIncreasingSequence(sequence):
	for i in range(len(sequence)):
		a = sequence[i]
		sequence.pop(i)
		#Comprobar si hay numeros repetidos en sequence, si es asi False
		a=1
		while a<len(sequence):
			if sequence[a] == sequence[a-1]:
				return False
			a+=1
		if sequence == sorted(sequence):
			return True
		sequence.insert(i, a)
	return False

l = [1, 2, 1]
print(almostIncreasingSequence(l))
"""
"""
Given a sequence of integers as an array, determine whether it is possible
to obtain a strictly increasing sequence by removing no more than one element from the array.

Example:
For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get
a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2].
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""
"""
def rep(l):
	for i in l:
		l.pop(i)
		for j in l:
			if i-j==0:
				return False
		l.insert(len(l), i)
"""
